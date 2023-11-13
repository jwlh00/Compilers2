from prettytable import PrettyTable
from termcolor import colored

class Quadruple:

    def __init__(self, op, arg1, arg2, result):
        self.op = op 
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result


class TranslateToTACFunc():
    def __init__(self, tree, symbolTable):
        self.quadruplesList = [] 
        self.created_labels = set() 
        self.quadruplesDictionary = {} 
        self.nodesDone = set() 
        self.tree = tree 
        self.symbolTable = symbolTable 
        self.temp_counter = 1 
        self.label_counter = 1 
        self.index = 0  
        self.TAC = "" 
        self.readTree(tree.root) # Llama al método readTree con la raíz del árbol como argumento


    def createTemporal(self):

        # Crea una nueva variable temporal usando el contador de temporales (temp_counter)
        temp = f"t{self.temp_counter}"
        
        # Incrementa el contador de temporales para el próximo uso
        self.temp_counter += 1
        
        return temp


    def createLabel(self):

        # Crea una nueva etiqueta usando el contador de etiquetas (label_counter)
        label = f"L{self.label_counter}"
        
        # Incrementa el contador de etiquetas para el próximo uso
        self.label_counter += 1
        
        return label


    def readTree(self, node=None):

        # Verifica si el nodo proporcionado no es None
        if node is not None:
            
            # Llama al método FromYAPLToTAC para el nodo actual
            self.FromYAPLToTAC(node)
            
            # Itera sobre todos los hijos del nodo actual y llama recursivamente al método readTree para cada hijo
            for child in node.children:
                self.readTree(child)


    def FromYAPLToTAC(self, node=None):

        # Asigna el valor del nodo a la variable rule
        rule = node.val
        
        # Obtiene la cantidad de hijos del nodo y la almacena en la variable children_len
        children_len = len(node.children)
        
        if rule == "expr":
            
            # Comprueba si es un método sin parámetros
            if children_len == 3 and node.children[1].val == "(" and node.children[2].val == ")":
                self.methodCallQuad(node)

            # Comprueba si es un método con parámetros
            elif children_len > 3 and node.children[1].val == "(" and node.children[-1].val == ")":

                # self.quadruplesList.append(Quadruple("STACK_INIT","---","---","---"))
                self.methodCallParamsQuad(node)

                # self.quadruplesList.append(Quadruple("---","---","---","EMPTY_STACK"))
                
            # Comprueba si es operación aritmética
            elif children_len == 3 and node.children[1].val in ["+", "/", "-", "*"]:
                self.arithmeticQuad(node)
                
            # Comprueba si es un if
            
            elif children_len == 7 and node.children[0].val == "if" and node.children[-1].val == "fi":
                self.quadruplesList.append(Quadruple("IfHandler","---","---","---"))

                self.ifQuadEnhanced(node)

                # Quadruple comodin para ifelse:
                self.quadruplesList.append(Quadruple("---","---","---","END"))

            # Comprueba si es un while
            elif children_len == 5 and node.children[0].val == "while" and node.children[-1].val == "pool":

                self.quadruplesList.append(Quadruple("WhileHandler","---","---","---"))

                self.whileQuad(node)

                # Quadruple comodin para while:
                self.quadruplesList.append(Quadruple("---","---","---","END"))

            # Comprueba si es un return
            if node.children[0].val == "return":
                
                self.returnQuad(node)

        elif rule == "property":
            
            # Es una asignación de variable
            self.propertyQuad(node)
            
        elif rule == "varDeclaration":
            
            # Es una declaración de variable
            self.varDeclarationQuad(node)
            
        elif rule == "method":
            
            # Es un método
            self.methodQuad(node)
            
        elif rule == "classDefine":
            
            # Es una clase
            self.classQuad(node)



    # Agarramos los hijos de un nodo expr
    def getExprChildren(self, node, child_values=None):
        if child_values is None:
            child_values = []  # Inicializa la lista de valores de los hijos del nodo expr
        
        for child in node.children:
            if child.val == "expr":
                self.getExprChildren(child, child_values)  #Pasa la lista como argumento para que se mantenga entre llamadas recursivas
            else:
                child_values.append(child.val)
        
        return child_values
    
    # funcion para crear la cuadrupla de methodCall sin parametros
    def methodCallQuad(self, node):

        if node in self.nodesDone:
            return
        else:
            self.nodesDone.add(node)

        temp = self.createTemporal()

        cuadrupla = Quadruple("MethodHandler", node.children[0].val, 0, temp)
        self.quadruplesList.append(cuadrupla)

        # Agregamos el nodo a la lista de nodos procesados
        self.nodesDone.add(node)

        return temp

    # funcion para crear la cuadrupla de methodCall con parametros
    def methodCallParamsQuad(self, node):

        if node in self.nodesDone:
            return
        else:
            self.nodesDone.add(node)

        #saltarnos si es un return
        if node.children[0].val == "return":
            return
        #vemos si es algun print
        if node.children[0].val == "out_int" or node.children[0].val == 'out_string':
            argument = node.children[2].children[0].val
            self.quadruplesList.append(Quadruple("PROCEDURE", node.children[0].val, argument, None))
            return

        self.quadruplesList.append(Quadruple("STACK_INIT","---","---","---"))
        children = node.children
        # ver los formals
        contador = 0
        for child in children:
            if child.val == "expr":
                self.quadruplesList.append(Quadruple("PrepareParam", child.children[0].val, None, node.children[0].val))
                contador += 1
        
        # creamos el temporal
        temp = self.createTemporal()
        # creamos la cuadrupla
        cuadrupla = Quadruple("MethodHandler", node.children[0].val, contador, temp)
        self.quadruplesList.append(cuadrupla)
        self.quadruplesList.append(Quadruple("---","---","---","EMPTY_STACK"))

        return temp

    # funcion para crear la cuadrupla de if
    def ifQuadEnhanced(self, node=None, exit_label=None, start_label=None, primera_vez=True):

        if node in self.nodesDone:
            return

        if start_label is not None:

            self.quadruplesList.append(Quadruple("LabelHandler", None, None, start_label))

        # Este metodo esta creado para ser una version mejorada del ifQuad.

        # Un condicional if se ve de la siguiente manera: ['if', 'expr', 'then', 'expr', 'else', 'expr', 'fi']

        # Obtenemos la condición, el bloque then y el bloque else de los hijos del nodo

        cond_node, then_node, else_node = node.children[1], node.children[3], node.children[5]

        # Realizamos la cuadrupla de la condicion

        cond_quad = self.getExprChildren(cond_node)

        # Generamos una variable t para almacenar el result de la condicion

        t_condicion = self.createTemporal()

        # Generamos la cuadrupla de la condicion

        self.quadruplesList.append(Quadruple(cond_quad[1], cond_quad[0], cond_quad[2], t_condicion))

        # Una vez que tenemos el result de la condicion, creamos una etiqueta para el bloque then

        l_condicion = self.createLabel()

        # Creamos la cuadrupla de la etiqueta en caso de que la condicion sea falsa

        self.quadruplesList.append(Quadruple("IfNotHandler", t_condicion, None, l_condicion))

        # Creamos el cuerpo de la condicion then en caso de que la condicion sea verdadera

        # En el caso de que la condicion sea verdadera:
        cuad_tempr = self.readTree(then_node)

        # En este punto ya evaluamos el cuerpo del then, por lo que creamos una etiqueta para la salida del if

        if exit_label is None:

            exit_label = self.createLabel()
        
        # Creamos la cuadrupla de salto para salir del if

        self.quadruplesList.append(Quadruple("GotoHandler", None, None, exit_label))

        # Revismos si el cuerpo del else es otro if

        self.nodesDone.add(node)

        if else_node.children[0].val == "if":

            self.ifQuadEnhanced(else_node, exit_label, l_condicion, primera_vez=False)
        
        # Si el cuerpo del else no es otro if, entonces es un bloque de codigo normal

        else:

            self.quadruplesList.append(Quadruple("LabelHandler", None, None, l_condicion))

            self.readTree(else_node)

            self.quadruplesList.append(Quadruple("GotoHandler", None, None, exit_label))
        

        # Creamos la cuadrupla para la exit label del if

        if primera_vez:

            self.quadruplesList.append(Quadruple("LabelFinish", None, None, exit_label))

    # funcion para crear la cuadrupla de while
    def whileQuad(self, node=None):

        if node in self.nodesDone:
            return
        else:
            self.nodesDone.add(node)

        # Creamos un label para el comienzo del while

        start_label = self.createLabel()

        # Creamos la cuadrupla del label

        self.quadruplesList.append(Quadruple("LabelHandler", None, None, start_label))

        # Creamos un label para el final del while

        exit_label = self.createLabel()

        # Obtenemos el cuerpo del while

        condicion, cuerpo = node.children[1], node.children[3]

        cuad_condicion = self.getExprChildren(condicion)

        # Creamos una variable temporal para almacenar el result de la condicion

        t_condicion = self.createTemporal()

        # Creamos la cuadrupla de la condicion

        self.quadruplesList.append(Quadruple(cuad_condicion[1], cuad_condicion[0], cuad_condicion[2], t_condicion))

        # Creamos la cuadrupla de salto en caso de que la condicion sea falsa

        self.quadruplesList.append(Quadruple("IfNotHandler", t_condicion, None, exit_label))

        # Creamos la/las cuadruplas del cuerpo del while

        self.readTree(cuerpo)

        # Creamos la cuadrupla de salto para volver a evaluar la condicion

        self.quadruplesList.append(Quadruple("GotoHandler", None, None, start_label))

        # Creamos la cuadrupla del label de salida del while

        self.quadruplesList.append(Quadruple("LabelFinish", None, None, exit_label))


    #if para ver si es asignacion o solo declaracion
    def propertyQuad(self, node=None):
        if len(node.children) > 1: # es una asignacion
            formal = node.children[0]
            expr = node.children[2]
            result = formal.children[0].val
            symbol = self.symbolTable.lookup_all(result)
            type = symbol.data_type

            cuadrupla = Quadruple("<-", expr.children[0].val, type, result)
            self.quadruplesList.append(cuadrupla)
        elif len(node.children) == 1: # es una declaracion
            formal = node.children[0]
            result = formal.children[0].val
            symbol = self.symbolTable.lookup_all(result)
            type = symbol.data_type

            if type == "Int":
                cuadrupla = Quadruple("<-", 0, type, result)
            elif type == "Bool":
                cuadrupla = Quadruple("<-", 'false', type, result)
            elif type == "String":
                cuadrupla = Quadruple("<-", '""', type, result)
            self.quadruplesList.append(cuadrupla)

    # funcion para crear la cuadrupla de returns
    def returnQuad(self, node=None):
        # Si el nodo tiene hijos
        if len(node.children) > 1:
            # Obtenemos los hijos del nodo VarDeclaration
            child_values = []
            for child in node.children:
                if child.val == "expr":
                    # Si el hijo es un nodo expr, llamamos recursivamente a arithmeticQuad(node)
                    child_values.append(self.arithmeticQuad(child))
                else:
                    # Si el hijo no es un nodo expr, simplemente agregamos su valor a la lista
                    child_values.append(child.val)
            
            # Creamos la cuadrupla con la operación de asignación y los operandos
            cuadrupla = Quadruple("ReturnHandler", child_values[2], None, None)
            
            # Agregamos la cuadrupla a la lista de cuadruplas
            self.quadruplesList.append(cuadrupla)
        else:
            # Si el nodo no tiene hijos o solo tiene uno, entonces es una variable o un número, y simplemente lo retornamos
            return node.val if len(node.children) == 0 else self.arithmeticQuad(node.children[0])

    # funcion para crear la cuadrupla de variables asignadas
    def varDeclarationQuad(self, node=None):
        if node in self.nodesDone:
            return
        else:
            self.nodesDone.add(node)

        # Si el nodo tiene hijos
        if len(node.children) > 1:
            # Obtenemos los hijos del nodo VarDeclaration
            child_values = []
            for child in node.children:
                if child.val == "expr":
                    # Si el hijo es un nodo expr, llamamos recursivamente a arithmeticQuad(node)

                    # Si es un parametro llamamos a methodCallParamsQuad

                    # Comprueba si es un método sin parámetros
            
                    children_len = len(child.children)

                    if children_len == 3 and child.children[1].val == "(" and child.children[2].val == ")":
                        
                        temp = self.methodCallQuad(child)

                        child_values.append(temp)
                        
                    # Comprueba si es un método con parámetros
                    
                    elif children_len > 3 and child.children[1].val == "(" and child.children[-1].val == ")":
                        temp = self.methodCallParamsQuad(child)

                        child_values.append(temp)

                    else:
                        temp = self.arithmeticQuad(child)

                        child_values.append(temp)
                else:
                    # Si el hijo no es un nodo expr, simplemente agregamos su valor a la lista
                    child_values.append(child.val)
            
            # Creamos la cuadrupla con la operación de asignación y los operandos
            cuadrupla = Quadruple("<-", child_values[2], None, child_values[0])
            
            # Agregamos la cuadrupla a la lista de cuadruplas
            self.quadruplesList.append(cuadrupla)
            return cuadrupla

    # funcion para crear la cuadrupla de operaciones aritmeticas
    def arithmeticQuad(self, node=None):
        # Si el nodo ya ha sido procesado, simplemente retornamos su valor
        if node in self.nodesDone:
            return

        # Si el nodo tiene hijos
        if len(node.children) > 1:
            # Obtenemos los hijos del nodo expr
            child_values = []
            for child in node.children:
                if child.val == "expr":
                    # Si el hijo es un nodo expr, llamamos recursivamente a arithmeticQuad(node)
                    child_values.append(self.arithmeticQuad(child))
                elif child.val in ["(", ")"]:
                    # Si el hijo es un paréntesis, lo ignoramos
                    continue
                else:
                    # Si el hijo no es un nodo expr ni un paréntesis, simplemente agregamos su valor a la lista
                    child_values.append(child.val)
            
            # Si hay suficientes valores en child_values para formar una cuadrupla
            if len(child_values) >= 3:
                # Creamos un nuevo temporal para almacenar el result de la operación
                temp = self.createTemporal()
                
                # Creamos la cuadrupla con la operación y los operandos
                cuadrupla = Quadruple(child_values[1], child_values[0], child_values[2], temp)
                # print(cuadrupla)
                
                # Agregamos la cuadrupla a la lista de cuadruplas
                self.quadruplesList.append(cuadrupla)
                
                # Agregamos el nodo a la lista de nodos procesados
                self.nodesDone.add(node)

                # Retornamos el temporal que almacena el result de la operación
                return temp
            else:
                # Si no hay suficientes valores en child_values, simplemente retornamos el primer valor
                return child_values[0] if child_values else None
        else:
            # Si el nodo no tiene hijos o solo tiene uno, entonces es una variable o un número, y simplemente lo retornamos
            return node.val if len(node.children) == 0 else self.arithmeticQuad(node.children[0])

    # funcion para crear la cuadrupla de metodo
    def methodQuad(self, node=None):

        children = node.children
        
        # creamos la cuadrupla
        cuadrupla = Quadruple("CreateMethod", node.children[0].val, node.children[-4].val, None)
        self.quadruplesList.append(cuadrupla)

        for child in children:
            if child.val == "formal":
                self.paramQuad(child, node.children[0].val)
    
    # funcion para crear la cuadrupla de clase
    def classQuad(self, node=None):

        # Revisamos si la clase incluye herencia

        if node.children[2].val == "inherits":

            cuadrupla = Quadruple("class", node.children[1].val, node.children[3].val, None)

            self.quadruplesList.append(cuadrupla)
        
        # La clase no incluye herencia

        else:

            cuadrupla = Quadruple("class", node.children[1].val, None, None)

            self.quadruplesList.append(cuadrupla)

    # funcion para crear la cuadrupla de los parametros de un metodo
    def paramQuad(self, node=None, method=None):
            
        # creamos la cuadrupla
        cuadrupla = Quadruple("Param", node.children[0].val, node.children[2].val, method)
        self.quadruplesList.append(cuadrupla)

    # funcion para traducir las cuadruplas a codigo de tres direcciones
    def translate(self):

        codigo_tres_direcciones = ""
        indent_level = 0

        for cuadrupla in self.quadruplesList:
            if cuadrupla.op == "class":
                indent_level = 0
                codigo_tres_direcciones += " " * indent_level + f"class {cuadrupla.arg1}:\n"
                indent_level += 4
            elif cuadrupla.op == "CreateMethod":
                codigo_tres_direcciones += " " * indent_level + f"function {cuadrupla.arg1}, {cuadrupla.arg2}:\n"
                indent_level += 4
            elif cuadrupla.op == "IfHandler":
                codigo_tres_direcciones += " " * indent_level + "if:\n"
                indent_level += 4
            elif cuadrupla.op == "WhileHandler":
                codigo_tres_direcciones += " " * indent_level + "while:\n"
                indent_level += 4
            elif cuadrupla.op == "LabelFinish":
                indent_level -= 4
                codigo_tres_direcciones += " " * indent_level + f"{cuadrupla.result} exit\n"
            elif cuadrupla.op in ["+", "/", "-", "*", "<", ">", "=", "<=", ">="]:
                codigo_tres_direcciones += f"{' ' * indent_level}{cuadrupla.result} = {cuadrupla.arg1} {cuadrupla.op} {cuadrupla.arg2}\n"
            elif cuadrupla.op == "<-":
                codigo_tres_direcciones += f"{' ' * indent_level}{cuadrupla.result} = {cuadrupla.arg1}\n"
            elif cuadrupla.op == "PrepareParam":
                codigo_tres_direcciones += f"{' ' * indent_level}param {cuadrupla.arg1}\n"
            elif cuadrupla.op == "MethodHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}{cuadrupla.result} = call {cuadrupla.arg1}, {cuadrupla.arg2}\n"
            elif cuadrupla.op == "Param":
                codigo_tres_direcciones += f"{' ' * indent_level}param {cuadrupla.arg1}, {cuadrupla.arg2}\n"
            elif cuadrupla.op == "ReturnHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}return {cuadrupla.arg1}\n"
                indent_level -= 4
            elif cuadrupla.op == "LabelHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}{cuadrupla.result}:\n"
            elif cuadrupla.op == "IfNotHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}if not {cuadrupla.arg1}, goto {cuadrupla.result}\n"
            elif cuadrupla.op == "GotoHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}goto {cuadrupla.result}\n"

        self.TAC = codigo_tres_direcciones
        return codigo_tres_direcciones

    def __str__(self):
        # Header
        quadruple_str = "\n---------------CUADRUPLAS---------------\n"

        # Loop through the quadruples and append them to the string
        for cuadrupla in self.quadruplesList:
            quadruple_str += f"({self.quadruplesList.index(cuadrupla)}, {cuadrupla.op}, {cuadrupla.arg1}, {cuadrupla.arg2}, {cuadrupla.result})\n"

        # Return the final string representation
        return quadruple_str



