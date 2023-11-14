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
        self.readTree(tree.root)


    def createTemporal(self):
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp


    def createLabel(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label


    def readTree(self, node=None):
        if node is not None:
            self.FromYAPLToTAC(node)
            for child in node.children:
                self.readTree(child)


    def FromYAPLToTAC(self, node=None):
        rule = node.val
        children_len = len(node.children)
        if rule == "expr":
            if children_len == 3 and node.children[1].val == "(" and node.children[2].val == ")":
                self.methodCallQuad(node)

            elif children_len > 3 and node.children[1].val == "(" and node.children[-1].val == ")":
                self.methodCallParamsQuad(node)

            elif children_len == 3 and node.children[1].val in ["+", "/", "-", "*"]:
                self.arithmeticQuad(node)
                
            elif children_len == 7 and node.children[0].val == "if" and node.children[-1].val == "fi":
                self.quadruplesList.append(Quadruple("IfHandler","---","---","---"))
                self.ifQuadEnhanced(node)
                self.quadruplesList.append(Quadruple("---","---","---","END"))

            elif children_len == 5 and node.children[0].val == "while" and node.children[-1].val == "pool":
                self.quadruplesList.append(Quadruple("WhileHandler","---","---","---"))
                self.whileQuad(node)
                self.quadruplesList.append(Quadruple("---","---","---","END"))

            if node.children[0].val == "return":
                self.returnQuad(node)

        elif rule == "property":
            self.propertyQuad(node)

        elif rule == "varDeclaration":
            self.varDeclarationQuad(node)
            
        elif rule == "method":
            self.methodQuad(node)
            
        elif rule == "classDefine":
            self.classQuad(node)


    def getExprChildren(self, node, child_values=None):
        if child_values is None:
            child_values = []
        
        for child in node.children:
            if child.val == "expr":
                self.getExprChildren(child, child_values) 
            else:
                child_values.append(child.val)
        
        return child_values
    
    def methodCallQuad(self, node):
        if node in self.nodesDone:
            return
        else:
            self.nodesDone.add(node)
        temp = self.createTemporal()

        quadruple = Quadruple("MethodHandler", node.children[0].val, 0, temp)
        self.quadruplesList.append(quadruple)
        self.nodesDone.add(node)
        return temp

    def methodCallParamsQuad(self, node):
        if node in self.nodesDone:
            return
        else:
            self.nodesDone.add(node)

        if node.children[0].val == "return":
            return
        if node.children[0].val == "out_int" or node.children[0].val == 'out_string':
            argument = node.children[2].children[0].val
            self.quadruplesList.append(Quadruple("PROCEDURE", node.children[0].val, argument, None))
            return
        self.quadruplesList.append(Quadruple("STACK_INIT","---","---","---"))
        children = node.children
        contador = 0
        for child in children:
            if child.val == "expr":
                self.quadruplesList.append(Quadruple("PrepareParam", child.children[0].val, None, node.children[0].val))
                contador += 1
        
        temp = self.createTemporal()
        quadruple = Quadruple("MethodHandler", node.children[0].val, contador, temp)
        self.quadruplesList.append(quadruple)
        self.quadruplesList.append(Quadruple("---","---","---","EMPTY_STACK"))
        return temp

    def ifQuadEnhanced(self, node=None, exit_label=None, start_label=None, primera_vez=True):
        if node in self.nodesDone:
            return
        if start_label is not None:
            self.quadruplesList.append(Quadruple("LabelHandler", None, None, start_label))
        cond_node, then_node, else_node = node.children[1], node.children[3], node.children[5]
        cond_quad = self.getExprChildren(cond_node)
        t_condicion = self.createTemporal()
        self.quadruplesList.append(Quadruple(cond_quad[1], cond_quad[0], cond_quad[2], t_condicion))
        l_condicion = self.createLabel()

        self.quadruplesList.append(Quadruple("IfNotHandler", t_condicion, None, l_condicion))
        cuad_tempr = self.readTree(then_node)

        if exit_label is None:
            exit_label = self.createLabel()

        self.quadruplesList.append(Quadruple("GotoHandler", None, None, exit_label))
        self.nodesDone.add(node)

        if else_node.children[0].val == "if":
            self.ifQuadEnhanced(else_node, exit_label, l_condicion, primera_vez=False)
        else:
            self.quadruplesList.append(Quadruple("LabelHandler", None, None, l_condicion))
            self.readTree(else_node)
            self.quadruplesList.append(Quadruple("GotoHandler", None, None, exit_label))
        
        if primera_vez:
            self.quadruplesList.append(Quadruple("LabelFinish", None, None, exit_label))

    def whileQuad(self, node=None):
        if node in self.nodesDone:
            return
        else:
            self.nodesDone.add(node)
        start_label = self.createLabel()
        self.quadruplesList.append(Quadruple("LabelHandler", None, None, start_label))
        exit_label = self.createLabel()
        condicion, cuerpo = node.children[1], node.children[3]
        cuad_condicion = self.getExprChildren(condicion)
        t_condicion = self.createTemporal()

        self.quadruplesList.append(Quadruple(cuad_condicion[1], cuad_condicion[0], cuad_condicion[2], t_condicion))
        self.quadruplesList.append(Quadruple("IfNotHandler", t_condicion, None, exit_label))
        self.readTree(cuerpo)
        self.quadruplesList.append(Quadruple("GotoHandler", None, None, start_label))
        self.quadruplesList.append(Quadruple("LabelFinish", None, None, exit_label))

    def propertyQuad(self, node=None):
        if len(node.children) > 1:
            formal = node.children[0]
            expr = node.children[2]
            result = formal.children[0].val
            symbol = self.symbolTable.lookup_all(result)
            type = symbol.data_type
            quadruple = Quadruple("<-", expr.children[0].val, type, result)
            self.quadruplesList.append(quadruple)

        elif len(node.children) == 1:
            formal = node.children[0]
            result = formal.children[0].val
            symbol = self.symbolTable.lookup_all(result)
            type = symbol.data_type

            if type == "Int":
                quadruple = Quadruple("<-", 0, type, result)
            elif type == "Bool":
                quadruple = Quadruple("<-", 'false', type, result)
            elif type == "String":
                quadruple = Quadruple("<-", '""', type, result)
            self.quadruplesList.append(quadruple)

    def returnQuad(self, node=None):
        if len(node.children) > 1:
            child_values = []
            for child in node.children:
                if child.val == "expr":
                    child_values.append(self.arithmeticQuad(child))
                else:
                    child_values.append(child.val)
            quadruple = Quadruple("ReturnHandler", child_values[2], None, None)
            self.quadruplesList.append(quadruple)
        else:
            return node.val if len(node.children) == 0 else self.arithmeticQuad(node.children[0])

    def varDeclarationQuad(self, node=None):
        if node in self.nodesDone:
            return
        else:
            self.nodesDone.add(node)

        if len(node.children) > 1:
            child_values = []
            for child in node.children:
                if child.val == "expr":
                    children_len = len(child.children)
                    if children_len == 3 and child.children[1].val == "(" and child.children[2].val == ")":
                        temp = self.methodCallQuad(child)
                        child_values.append(temp)
                        
                    elif children_len > 3 and child.children[1].val == "(" and child.children[-1].val == ")":
                        temp = self.methodCallParamsQuad(child)
                        child_values.append(temp)
                    else:
                        temp = self.arithmeticQuad(child)
                        child_values.append(temp)
                else:
                    child_values.append(child.val)
            quadruple = Quadruple("<-", child_values[2], None, child_values[0])
            
            self.quadruplesList.append(quadruple)
            return quadruple

    def arithmeticQuad(self, node=None):
        if node in self.nodesDone:
            return
        if len(node.children) > 1:
            child_values = []
            for child in node.children:
                if child.val == "expr":
                    child_values.append(self.arithmeticQuad(child))
                elif child.val in ["(", ")"]:
                    continue
                else:
                    child_values.append(child.val)
            
            if len(child_values) >= 3:
                temp = self.createTemporal()
                quadruple = Quadruple(child_values[1], child_values[0], child_values[2], temp)
                self.quadruplesList.append(quadruple)
                self.nodesDone.add(node)
                return temp
            else:
                return child_values[0] if child_values else None
        else:
            return node.val if len(node.children) == 0 else self.arithmeticQuad(node.children[0])

    def methodQuad(self, node=None):
        children = node.children
        quadruple = Quadruple("CreateMethod", node.children[0].val, node.children[-4].val, None)
        self.quadruplesList.append(quadruple)

        for child in children:
            if child.val == "formal":
                self.paramQuad(child, node.children[0].val)
    
    def classQuad(self, node=None):
        if node.children[2].val == "inherits":
            quadruple = Quadruple("class", node.children[1].val, node.children[3].val, None)
            self.quadruplesList.append(quadruple)
        
        else:
            quadruple = Quadruple("class", node.children[1].val, None, None)
            self.quadruplesList.append(quadruple)

    def paramQuad(self, node=None, method=None):
        quadruple = Quadruple("Param", node.children[0].val, node.children[2].val, method)
        self.quadruplesList.append(quadruple)

    def translate(self):
        codigo_tres_direcciones = ""
        indent_level = 0

        for quadruple in self.quadruplesList:
            if quadruple.op == "class":
                indent_level = 0
                codigo_tres_direcciones += " " * indent_level + f"class {quadruple.arg1}:\n"
                indent_level += 4
            elif quadruple.op == "CreateMethod":
                codigo_tres_direcciones += " " * indent_level + f"function {quadruple.arg1}, {quadruple.arg2}:\n"
                indent_level += 4
            elif quadruple.op == "IfHandler":
                codigo_tres_direcciones += " " * indent_level + "if:\n"
                indent_level += 4
            elif quadruple.op == "WhileHandler":
                codigo_tres_direcciones += " " * indent_level + "while:\n"
                indent_level += 4
            elif quadruple.op == "LabelFinish":
                indent_level -= 4
                codigo_tres_direcciones += " " * indent_level + f"{quadruple.result} exit\n"
            elif quadruple.op in ["+", "/", "-", "*", "<", ">", "=", "<=", ">="]:
                codigo_tres_direcciones += f"{' ' * indent_level}{quadruple.result} = {quadruple.arg1} {quadruple.op} {quadruple.arg2}\n"
            elif quadruple.op == "<-":
                codigo_tres_direcciones += f"{' ' * indent_level}{quadruple.result} = {quadruple.arg1}\n"
            elif quadruple.op == "PrepareParam":
                codigo_tres_direcciones += f"{' ' * indent_level}param {quadruple.arg1}\n"
            elif quadruple.op == "MethodHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}{quadruple.result} = call {quadruple.arg1}, {quadruple.arg2}\n"
            elif quadruple.op == "Param":
                codigo_tres_direcciones += f"{' ' * indent_level}param {quadruple.arg1}, {quadruple.arg2}\n"
            elif quadruple.op == "ReturnHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}return {quadruple.arg1}\n"
                indent_level -= 4
            elif quadruple.op == "LabelHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}{quadruple.result}:\n"
            elif quadruple.op == "IfNotHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}if not {quadruple.arg1}, goto {quadruple.result}\n"
            elif quadruple.op == "GotoHandler":
                codigo_tres_direcciones += f"{' ' * indent_level}goto {quadruple.result}\n"

        self.TAC = codigo_tres_direcciones
        return codigo_tres_direcciones

    def __str__(self):
        quadruple_str = "\n---------------QUADRUPLES---------------\n"

        for quadruple in self.quadruplesList:
            quadruple_str += f"({self.quadruplesList.index(quadruple)}, {quadruple.op}, {quadruple.arg1}, {quadruple.arg2}, {quadruple.result})\n"

        return quadruple_str



