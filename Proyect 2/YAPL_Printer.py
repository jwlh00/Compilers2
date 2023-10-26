from YAPLListener import YAPLListener
from YAPLParser import YAPLParser
from itertools import groupby
from antlr4.tree.Trees import TerminalNode
from antlr4.error.ErrorListener import ErrorListener
from symbol_table import *
import re

class YAPLPrinter(YAPLListener):
    def __init__(self) -> None:
        self.root = None

        self.STRING = "string"
        self.INT = "int"
        self.BOOL = "bool"
        self.IO = "io"
        self.VOID = "void"
        self.ERROR = "error"
        self.OBJECT = "object"
        self.SELF_TYPE = "self_type"

        self.basic_data_type = {
            'string': self.STRING,
            'int': self.INT,
            'bool': self.BOOL,
        }

        self.default_data_types = {
            'string': self.STRING,
            'int': self.INT,
            'bool': self.BOOL,
            'io': self.IO,
            'void': self.VOID,
            'object': self.OBJECT,
            'error': self.ERROR,
            'self_type': self.SELF_TYPE
        }

        self.default_methods = MethodTable()
        # OBJECT
        self.default_methods.add('object', 'abort', [], 'global -> object', hex(id(self)), 'Linea: 0 Columna: 0')
        self.default_methods.add('string', 'type_name', [], 'global -> object', hex(id(self)), 'Linea: 0 Columna: 0')
        self.default_methods.add('SELF_TYPE', 'copy', [], 'global -> object', hex(id(self)), 'Linea: 0 Columna: 0')
        #IO
        self.default_methods.add('SELF_TYPE', 'out_string', ['x:string'], 'global -> io', hex(id(self)), 'Linea: 0 Columna: 0')
        self.default_methods.add('SELF_TYPE', 'out_int', ['x:int'], 'global -> io', hex(id(self)), 'Linea: 0 Columna: 0')
        self.default_methods.add('string', 'in_string', [], 'global -> io', hex(id(self)), 'Linea: 0 Columna: 0')
        self.default_methods.add('int', 'in_int', [], 'global -> io', hex(id(self)), 'Linea: 0 Columna: 0')
        #STRING
        self.default_methods.add('int', 'length', [], 'global -> string', hex(id(self)), 'Linea: 0 Columna: 0')
        self.default_methods.add('string', 'concat', ['s:string'], 'global -> string', hex(id(self)), 'Linea: 0 Columna: 0')
        self.default_methods.add('string', 'substr', ['i:int', 'l:int'], 'global -> string', hex(id(self)), 'Linea: 0 Columna: 0')


        # Saves current return values
        self.current_return_values = []

        self.scopes = []
        self.current_scope = None
        self.current_scope_statement = []
        self.current_scope_class = None
        self.sizeOf_scope = 0
        # self.type_table = TypeTable()
        self.global_symbol_table = SymbolTable()
        self.errors = SemanticError()
        self.global_method_table = MethodTable() # Saves ALL the methods
        self.global_method_call_table = MethodCallTable() # Saves ALL the method calls
        self.method_table = MethodTable() # Saves the methods of the current scope
        self.method_call_table = MethodCallTable() # Saves the method calls of the current scope
        self.class_table = ClassTable()

        self.node_type = {}

    
    def popscope(self, merging = False):
        if merging == False:
            self.current_scope.totable()
            self.current_scope = self.scopes.pop()
        else:
            self.current_scope.totable()
            self.current_scope._symbols = self.current_scope._symbols + self.scopes.pop()._symbols 
    
    def newscope(self, goingToLocal = False):
        if goingToLocal == False:
            self.scopes.append(self.current_scope)
        else:
            self.scopes.append(self.current_scope)
            self.current_scope = SymbolTable()
    
    def find(self, var):
        lookup = self.current_scope.lookup(var)
        if lookup == 0:
            scope_reverse = self.scopes.copy()
            scope_reverse.reverse()
            for scope in scope_reverse:
                lookup2 = scope.lookup(var)
                if lookup2 != 0:
                    return lookup2
            return 0
        else:
            return lookup
        
    def intersection(self, a, b):
        return [v for v in a if v in b]
    
    def allequal(self, iterable):
        g = groupby(iterable)
        return next(g, True) and not next(g, False)
    
    def childrenhaserror(self, ctx):
        non_terminals = [self.node_type[i] for i in ctx.children if type(i) in [YAPLParser.LocationContext, YAPLParser.ExprContext, YAPLParser.BlockContext, YAPLParser.DeclarationContext]]
        if self.ERROR in non_terminals:
            return True
        return False

    def enterProgram(self, ctx: YAPLParser.ProgramContext):
        print(" --- INICIO PROGRAMA --- ")
        self.root = ctx
        self.current_scope = SymbolTable()
        self.current_scope_statement.append("global")
        
    
    def enterClas_list(self, ctx: YAPLParser.Clas_listContext):
        line = ctx.type_()[0].start.line
        col = ctx.type_()[0].start.column
        address = hex(id(ctx))
        class_type = ctx.type_()[0].getText()            


        position = "Linea: " + str(line) + " Columna: " + str(col)
        try:
            inheritance = ctx.type_()[1].getText()
        except:
            inheritance = None

        # Check for recursive inheritance
        if inheritance is not None:
            if inheritance == class_type:
                self.errors.add(line, col, "Herencia a si mismo no es permitido: " + inheritance)

        
        # Error si clase main es heredada por otra clase
        if inheritance is not None:
            # Default data types cannot be inherited
            if inheritance.lower() in self.default_data_types:
                self.errors.add(line, col, "Tipo basico no puede ser heredado: " + inheritance)

        if class_type.lower() == 'main': # Error si clase main hereda de otra clase
            if inheritance is not None:
                self.errors.add(line, col, "Main no puede heredar de otra clase")

        if self.class_table.lookup(class_type) == 0:
            self.class_table.add(class_type, class_type, self.current_scope_statement[-1], position, inheritance, address)
        
        else: # Error si hay clases duplicadas
            line = ctx.type_()[0].start.line
            col = ctx.type_()[0].start.column
            self.errors.add(line, col, "Clase duplicada: " + class_type)
        
        self.current_scope_statement.append("global -> " + class_type)
        self.current_scope_class = self.current_scope_statement[-1]
        self.newscope()

        # Add inherited variables to current scope
        if inheritance is not None:
            inherited_symbols = self.global_symbol_table._symbols.copy()
            # print('inherited_symbols', inherited_symbols)
            for symbol in inherited_symbols:
                if symbol['Scope'] == 'global -> ' + inheritance:
                    if symbol['IsInherited'] == False:
                        self.current_scope.add(symbol['Type'], symbol['ID'], self.current_scope_statement[-1], symbol['Value'], symbol['Position'], symbol['Address'], symbol['IsParameter'], True)
                        self.global_symbol_table.add(symbol['Type'], symbol['ID'], self.current_scope_statement[-1], symbol['Value'], symbol['Position'], symbol['Address'], symbol['IsParameter'], True)
                        
                    else:
                        pass # No se agregan variables heredadas de variables heredadas (Evita herencia multiple)
            
            # Add inherited methods to current scope
            inherited_methods = self.global_method_table._methods.copy()
            for method in inherited_methods:
                if method['Scope'] == 'global -> ' + inheritance:
                    if method['IsInherited'] == False and method['ID'] != 'init':
                        self.method_table.add(method['Type'], method['ID'], method['Parameters'], self.current_scope_statement[-1], method['Address'], method['Position'], True)
                        self.global_method_table.add(method['Type'], method['ID'], method['Parameters'], self.current_scope_statement[-1], method['Address'], method['Position'], True)
                    else:
                        pass # No se agregan metodos heredados de metodos heredados (Evita herencia multiple)

    # Entrando a declaraciones de variables
    def enterAttribute_definition(self, ctx: YAPLParser.Attribute_definitionContext):
        tipo = ctx.type_().getText()
        address = hex(id(ctx))
        position = "Linea: " + str(ctx.type_().start.line) + " Columna: " + str(ctx.type_().start.column)

        value = ctx.expr().pop().getText() if len(ctx.expr()) > 0 else None

        copy_global_symbol_table = self.global_symbol_table._symbols.copy()
        for symbol in copy_global_symbol_table:
            # Check if current scope is local
            if self.current_scope_statement[-1] == 'local':
                if symbol['Scope'] == self.current_scope_class:
                    self.current_scope._symbols.append(symbol)

        if value is not None and value != self.VOID: # Si hay valor convertir a tipo de dato esperado
            if tipo.lower() == self.basic_data_type['string']:
                # Check if value is a string with regex
                if value.startswith("'") and value.endswith("'"):
                    value = str(value)
                elif value.startswith('"') and value.endswith('"'):
                    value = str(value)
                else:
                    # Check if value is a valid ID
                    if self.current_scope.lookup(value) == 0:
                        line = ctx.type_().start.line
                        col = ctx.type_().start.column
                        self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido para string: " + value)
                    else:
                        lookupvalue = self.current_scope.lookup(value)
                        if lookupvalue['Type'].lower() != 'string':
                            line = ctx.type_().start.line
                            col = ctx.type_().start.column
                            self.errors.add(line,col,"Variable asignada no es de tipo string: " + value)

            elif tipo.lower() == self.basic_data_type['int']:

                if "+" in value or "-" in value or "*" in value or "/" in value:
                    if is_valid_arithmethic_expression(value):
                            # Check if value is a valid digit
                            operation_values = re.split(r'[-+*/]', value)
                            operation_values = [operation_values.strip() for operation_values in operation_values if operation_values.strip()]
                            for token in operation_values:
                                if token.isdigit() == False:
                                    if self.current_scope.lookup(token) == 0:
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para operacion aritmetica: " + token)
                                    else:
                                        lookupvalue = self.current_scope.lookup(token)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.expr().start.line
                                            col = ctx.expr().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + token)

                            
                    else:
                        line = ctx.type_().start.line
                        col = ctx.type_().start.column
                        self.errors.add(line,col,"Expresion aritmetica invalida: " + value)
                else:
                    # Check if value is digit
                    if value.isdigit():
                        value = int(value)
                    elif value == 'true' or value == 'false':
                        if value == 'true':
                            value = 1
                        elif value == 'false':
                            value = 0

                    else:
                        # Check if value is a valid ID
                        if self.current_scope.lookup(value) == 0:
                            line = ctx.type_().start.line
                            col = ctx.type_().start.column
                            self.errors.add(line,col,"La variable asignada no existe aun: " + value)
                        else:
                            lookupvalue = self.current_scope.lookup(value)
                            if lookupvalue['Type'].lower() != 'int' and lookupvalue['Type'].lower() != 'bool':
                                line = ctx.type_().start.line
                                col = ctx.type_().start.column
                                self.errors.add(line,col,"Variable asignada no es tipo int: " + value)


            elif tipo.lower() == self.basic_data_type['bool']:
                if is_valid_boolean_expression(value):
                    value = bool(value)
                elif value.isdigit():
                    value = int(value)
                    if value < 1:
                        value = False
                    else:
                        value = True
                else:
                    if is_valid_comparison_operation(value):
                        
                        if "<" in value:
                            valueOne = value.split("<")[0]
                            valueTwo = value.split("<")[1]

                            if valueOne.isdigit() and valueTwo.isdigit():
                                pass
                            else:
                                # Check if value is a valid ID
                                if valueOne.isdigit() == False:
                                    if self.current_scope.lookup(valueOne) == 0:
                                        line = ctx.type_().start.line
                                        col = ctx.type_().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                                    else:
                                        lookupvalue = self.current_scope.lookup(valueOne)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.type_().start.line
                                            col = ctx.type_().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + valueOne)

                                if valueTwo.isdigit() == False:
                                    if self.current_scope.lookup(valueTwo) == 0:
                                        line = ctx.type_().start.line
                                        col = ctx.type_().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                                    else:
                                        lookupvalue = self.current_scope.lookup(valueTwo)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.type_().start.line
                                            col = ctx.type_().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + valueTwo)

                        elif "<=" in value:
                            valueOne = value.split("<=")[0]
                            valueTwo = value.split("<=")[1]

                            if valueOne.isdigit() and valueTwo.isdigit():
                                pass
                            else:
                                # Check if value is a valid ID
                                if valueOne.isdigit() == False:
                                    if self.current_scope.lookup(valueOne) == 0:
                                        line = ctx.type_().start.line
                                        col = ctx.type_().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                                    else:
                                        lookupvalue = self.current_scope.lookup(valueOne)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.type_().start.line
                                            col = ctx.type_().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + valueOne)

                                if valueTwo.isdigit() == False:
                                    if self.current_scope.lookup(valueTwo) == 0:
                                        line = ctx.type_().start.line
                                        col = ctx.type_().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                                    else:
                                        lookupvalue = self.current_scope.lookup(valueTwo)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.type_().start.line
                                            col = ctx.type_().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + valueTwo)
                                            

                        elif "=" in value:
                            valueOne= value.split("=")[0]
                            valueTwo = value.split("=")[1]
                            # Check if they are same type
                            if valueOne.isdigit() and valueTwo.isdigit():
                                pass
                            else:
                                # Check if value is a valid ID
                                lookupValueOne = self.current_scope.lookup(valueOne)
                                lookupValueTwo = self.current_scope.lookup(valueTwo)

                                if lookupValueOne == 0 and lookupValueTwo == 0:

                                    # Check if values are strings
                                    if valueOne.startswith('"') and valueOne.endswith('"') and valueTwo.startswith('"') and valueTwo.endswith('"'):
                                        pass
                                    elif valueOne.isdigit() and valueTwo.isdigit():
                                        pass    
                                    elif valueOne == 'true' or valueOne == 'false' and valueTwo == 'true' or valueTwo == 'false':
                                        pass
                                    else:
                                        line = ctx.type_().start.line
                                        col = ctx.type_().start.column
                                        self.errors.add(line,col,"Variables asignadas no existen aun o no son valores validos para comparacion: " + valueOne + "=" + valueTwo)
                                else:
                                    print("LookupValueOne", lookupValueOne)
                                    print("LookupValueTwo", lookupValueTwo)
                                    if lookupValueOne != 0 and lookupValueTwo != 0:
                                        # lookupvalue = self.current_scope.lookup(valueOne)
                                        if lookupValueOne['Type'].lower() != lookupValueTwo['Type'].lower():
                                            line = ctx.type_().start.line
                                            col = ctx.type_().start.column
                                            self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                    elif lookupValueOne == 0 and lookupValueTwo != 0:
                                        # check if value one is a string
                                        if valueOne.startswith('"') and valueOne.endswith('"'):
                                            if lookupValueTwo['Type'].lower() != 'string':
                                                line = ctx.type_().start.line
                                                col = ctx.type_().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                        # Check if value one is an int:
                                        elif valueOne.isdigit():
                                            if lookupValueTwo['Type'].lower() != 'int':
                                                line = ctx.type_().start.line
                                                col = ctx.type_().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                        
                                        # Check if value one is a boolean
                                        elif valueOne == 'true' or valueOne == 'false':
                                            if lookupValueTwo['Type'].lower() != 'bool':
                                                line = ctx.type_().start.line
                                                col = ctx.type_().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                        
                                        else:
                                            line = ctx.type_().start.line
                                            col = ctx.type_().start.column
                                            self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                                    elif lookupValueTwo == 0 and lookupValueOne != 0:
                                        # Check if value two is a string
                                        if valueTwo.startswith('"') and valueTwo.endswith('"'):
                                            if lookupValueOne['Type'].lower() != 'string':
                                                line = ctx.type_().start.line
                                                col = ctx.type_().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)
                                        # Check if value two is an int:
                                        elif valueTwo.isdigit():
                                            if lookupValueOne['Type'].lower() != 'int':
                                                line = ctx.type_().start.line
                                                col = ctx.type_().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)

                                        # Check if value two is a boolean
                                        elif valueTwo == 'true' or valueTwo == 'false':
                                            if lookupValueOne['Type'].lower() != 'bool':
                                                line = ctx.type_().start.line
                                                col = ctx.type_().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)
                                        else:
                                            line = ctx.type_().start.line
                                            col = ctx.type_().start.column
                                            self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                                            
                                        

                    else:
                        # Check if value is a valid ID
                        if self.current_scope.lookup(value) == 0:
                            line = ctx.type_().start.line
                            col = ctx.type_().start.column
                            self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para bool: " + value)
                        else:
                            lookupvalue = self.current_scope.lookup(value)
                            if lookupvalue['Type'].lower() != 'bool' and lookupvalue['Type'].lower() != 'int':
                                line = ctx.type_().start.line
                                col = ctx.type_().start.column
                                self.errors.add(line,col,"Variable asignada no es valida para tipo bool: " + value)                    
            else:
                # Check if value is a valid ID
                if self.current_scope.lookup(value) == 0:
                    line = ctx.type_().start.line
                    col = ctx.type_().start.column
                    self.errors.add(line,col,"Variable asignada no existe aun: " + value)
                else:
                    lookupvalue = self.current_scope.lookup(value)
                    if lookupvalue['Type'].lower() != tipo.lower():
                        line = ctx.type_().start.line
                        col = ctx.type_().start.column
                        self.errors.add(line,col,"Variable asignada no es de tipo: " + tipo + " " + value)
        
        if tipo.lower() not in self.default_data_types: # Buscar en tabla de clases si no es tipo basico
            if self.class_table.lookup(tipo) == 0:
                line = ctx.type_().start.line
                col = ctx.type_().start.column
                self.errors.add(line, col, "Tipo no existe: " + tipo)

        # Valores default si no se ha asignado previamente un valor a la variable
        if tipo.lower() in self.basic_data_type and value is None:
            if tipo.lower() == self.basic_data_type['string']:
                value = ""
            elif tipo.lower() == self.basic_data_type['int']:
                value = 0
            elif tipo.lower() == self.basic_data_type['bool']:
                value = False

        # Check recursive inheritance
        scope_split = self.current_scope_statement[-1].split(" -> ")
        if len(scope_split) > 1:
            if scope_split[1] == tipo:
                self.errors.add(ctx.type_().start.line, ctx.type_().start.column, "Herencia recursiva no permitida: " + tipo)

        if ctx.ID() is not None:
            ctx_id = ctx.ID().getText()

            if ctx_id == 'self':
                line = ctx.type_().start.line
                col = ctx.type_().start.column
                self.errors.add(line, col, "Variable no puede llamarse self: " + ctx_id)
            
            # Check if variable is a default data type
            if ctx_id.lower() in self.default_data_types:
                line = ctx.type_().start.line
                col = ctx.type_().start.column
                self.errors.add(line, col, "Variable no puede llamarse igual que un tipo basico: " + ctx_id)

            if self.current_scope.lookup(ctx_id) == 0:
                # Allow only simple inheritance
                self.current_scope.add(tipo, ctx_id, self.current_scope_statement[-1], value, position, address, False, False, self.class_table)
                self.global_symbol_table.add(tipo, ctx_id, self.current_scope_statement[-1], value, position, address, False, False, self.class_table)
            else:
                if self.current_scope.lookup(ctx_id)['IsInherited'] == True: # Overriding de variable heredada
                    inherited_symbol = self.current_scope.lookup(ctx_id)
                    if inherited_symbol['Type'].lower() == tipo.lower():
                        self.current_scope.delete(ctx_id)
                        # self.global_symbol_table.delete(ctx_id)
                        self.current_scope.add(tipo, ctx_id, self.current_scope_statement[-1], value, position, address, False, False, self.class_table)
                        self.global_symbol_table.add(tipo, ctx_id, self.current_scope_statement[-1], value, position, address, False, False, self.class_table)
                    else:
                        line = ctx.type_().start.line
                        col = ctx.type_().start.column
                        self.errors.add(line, col, "Variable heredada no puede cambiarse de tipo: " + ctx_id)
                else: # Error si hay variables duplicadas
                    if self.current_scope.lookup(ctx_id)['Scope'] != self.current_scope_statement[-1]:
                        self.current_scope.add(tipo, ctx_id, self.current_scope_statement[-1], value, position, address, False, False, self.class_table)
                        self.global_symbol_table.add(tipo, ctx_id, self.current_scope_statement[-1], value, position, address, False, False, self.class_table)
                    else:
                        line = ctx.type_().start.line
                        col = ctx.type_().start.column
                        self.errors.add(line, col, "Variable duplicada: " + ctx_id)
    
    def exitAttribute_definition(self, ctx: YAPLParser.Attribute_definitionContext):
        print('Saliendo de la declaracion de atributo: ' + ctx.ID().getText())

    
    def enterMethod_definition(self, ctx: YAPLParser.Method_definitionContext):
        method_id = ctx.ID().getText()
        method_type = None
        if ctx.type_():
            method_type = ctx.type_().getText()
            # Buscar en tabla de clases si no es tipo basico
            if method_type.lower() not in self.default_data_types:
                if self.class_table.lookup(method_type) == 0:
                    line = ctx.type_().start.line
                    col = ctx.type_().start.column
                    self.errors.add(line, col, "Tipo no existe: " + method_type)

        else:
            method_type = None
            self.errors.add(ctx.start.line, ctx.start.column, "Se debe especificar el tipo del metodo: " + method_id)
        address = hex(id(ctx))
        parameters = []
        if method_type:
            position = "Linea: " + str(ctx.type_().start.line) + " Columna: " + str(ctx.type_().start.column)
        else:
            position = "Linea: " + str(ctx.parameter_list().start.line) + " Columna: " + str(ctx.parameter_list().start.column)


        if self.method_table.lookup(method_id) == 0:
            self.global_method_table.add(method_type, method_id, parameters, self.current_scope_statement[-1], address, position)
            self.method_table.add(method_type, method_id, parameters, self.current_scope_statement[-1], address, position)
        else:

            if self.method_table.lookup(method_id)['IsInherited'] == True: # Overriding de metodo heredado
                inherited_method = self.method_table.lookup(method_id)
                if inherited_method['Type'].lower() == method_type.lower():
                    self.method_table.delete(method_id)
                    # self.global_method_table.delete(method_id)
                    self.method_table.add(method_type, method_id, parameters, self.current_scope_statement[-1], address, position)
                    self.global_method_table.add(method_type, method_id, parameters, self.current_scope_statement[-1], address, position)
                else:
                    line = ctx.type_().start.line
                    col = ctx.type_().start.column
                    self.errors.add(line, col, "Metodo heredado no puede cambiarse de tipo: " + method_id);
            else:
                line = ctx.type_().start.line
                col = ctx.type_().start.column
                self.errors.add(line, col, "Metodo duplicado: " + method_id)

        self.current_scope_statement.append("local")

        self.newscope(goingToLocal=True)

        parameter_list = ctx.parameter_list()
        if parameter_list is not None: # Si hay parametros
            formal_list = parameter_list.formal() # Parametros
            for formal in formal_list:
                formal_ctx = formal.getText()
                formal_name = formal_ctx.split(":")[0]
                formal_type = formal_ctx.split(":")[1]
                # Check that parameter name is not self or a default data type
                if formal_name == 'self':
                    line = ctx.parameter_list().start.line
                    col = ctx.parameter_list().start.column
                    self.errors.add(line, col, "Parametro no puede llamarse self: " + formal.ID().getText())
                elif formal_name.lower() in self.default_data_types:
                    line = ctx.parameter_list().start.line
                    col = ctx.parameter_list().start.column
                    self.errors.add(line, col, "Parametro no puede llamarse igual que un tipo basico: " + formal.ID().getText())
                else:
                    # Check if parameter type is a default data type
                    if formal_type.lower() in self.default_data_types:
                        parameters.append(formal.getText())

                        param_value = None
                        if formal_type.lower() == self.basic_data_type['string']:
                            param_value = ""

                        self.current_scope.add(formal_type, formal_name, self.current_scope_statement[-1], param_value, position, address, True, False)
                        self.global_symbol_table.add(formal_type, formal_name, self.current_scope_statement[-1], param_value, position, address, True, False)
                    else:
                        # Check if parameter type is a valid class
                        if self.class_table.lookup(formal_type) == 0:
                            line = ctx.parameter_list().start.line
                            col = ctx.parameter_list().start.column
                            self.errors.add(line, col, "Tipo especificado de parametro no existe: " + formal_type)
                        else:
                            parameters.append(formal.getText())
                            # Add parameter to local and global symbol table
                            self.current_scope.add(formal_type, formal_name, self.current_scope_statement[-1], None, position, address, True, False)
                            self.global_symbol_table.add(formal_type, formal_name, self.current_scope_statement[-1], None, position, address, True, False)

    def enterIf_statement(self, ctx: YAPLParser.If_statementContext):
        pass
        # self.current_scope_statement.append("local")
        # self.newscope()

    def exitIf_statement(self, ctx: YAPLParser.If_statementContext):
        
        condition = ctx.expr().getText()
        # Check if condition is valid
        if is_valid_boolean_expression(condition):
            pass
        else:
            # Check if its a comparison operation
            if is_valid_comparison_operation(condition):
                if "<" in condition and "<=" not in condition and "=" not in condition:
                    valueOne = condition.split("<")[0]
                    valueTwo = condition.split("<")[1]

                    if valueOne.isdigit() and valueTwo.isdigit():
                        pass
                    else:
                        # Check if value is a valid ID
                        if valueOne.isdigit() == False:
                            if self.current_scope.lookup(valueOne) == 0:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                            else:
                                lookupvalue = self.current_scope.lookup(valueOne)
                                if lookupvalue['Type'].lower() != 'int':
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no es tipo int: " + valueOne)
                                else:
                                    if lookupvalue == 0:
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o el input es invalido: " + valueOne)
                                    

                        if valueTwo.isdigit() == False:
                            if self.current_scope.lookup(valueTwo) == 0:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                            else:
                                lookupvalue = self.current_scope.lookup(valueTwo)
                                if lookupvalue['Type'].lower() != 'int':
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no es tipo int: " + valueTwo)

                elif "<=" in condition:
                    valueOne = condition.split("<=")[0]
                    valueTwo = condition.split("<=")[1]

                    if valueOne.isdigit() and valueTwo.isdigit():
                        pass
                    else:
                        # Check if value is a valid ID
                        if valueOne.isdigit() == False:
                            if self.current_scope.lookup(valueOne) == 0:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                            else:
                                lookupvalue = self.current_scope.lookup(valueOne)
                                if lookupvalue['Type'].lower() != 'int':
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no es tipo int: " + valueOne)

                        if valueTwo.isdigit() == False:
                            if self.current_scope.lookup(valueTwo) == 0:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                            else:
                                lookupvalue = self.current_scope.lookup(valueTwo)
                                if lookupvalue['Type'].lower() != 'int':
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no es tipo int: " + valueTwo)
                                    

                elif "=" in condition:
                    valueOne= condition.split("=")[0]
                    valueTwo = condition.split("=")[1]
                    # Check if they are same type
                    if valueOne.isdigit() and valueTwo.isdigit():
                        pass
                    else:
                        # Check if value is a valid ID
                        lookupValueOne = self.current_scope.lookup(valueOne)
                        lookupValueTwo = self.current_scope.lookup(valueTwo)

                        if lookupValueOne == 0 and lookupValueTwo == 0:

                            # Check if values are strings
                            if valueOne.startswith('"') and valueOne.endswith('"') and valueTwo.startswith('"') and valueTwo.endswith('"'):
                                pass
                            elif valueOne.isdigit() and valueTwo.isdigit():
                                pass    
                            elif valueOne == 'true' or valueOne == 'false' and valueTwo == 'true' or valueTwo == 'false':
                                pass
                            else:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variables asignadas no existen aun o no son valores validos para comparacion: " + valueOne + "=" + valueTwo)
                        else:
                            # print("LookupValueOne", lookupValueOne)
                            # print("LookupValueTwo", lookupValueTwo)
                            if lookupValueOne != 0 and lookupValueTwo != 0:
                                # lookupvalue = self.current_scope.lookup(valueOne)
                                if lookupValueOne['Type'].lower() != lookupValueTwo['Type'].lower():
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                            elif lookupValueOne == 0 and lookupValueTwo != 0:
                                # check if value one is a string
                                if valueOne.startswith('"') and valueOne.endswith('"'):
                                    if lookupValueTwo['Type'].lower() != 'string':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                # Check if value one is an int:
                                elif valueOne.isdigit():
                                    if lookupValueTwo['Type'].lower() != 'int':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                
                                # Check if value one is a boolean
                                elif valueOne == 'true' or valueOne == 'false':
                                    if lookupValueTwo['Type'].lower() != 'bool':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                
                                else:
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                            elif lookupValueTwo == 0 and lookupValueOne != 0:
                                # Check if value two is a string
                                if valueTwo.startswith('"') and valueTwo.endswith('"'):
                                    if lookupValueOne['Type'].lower() != 'string':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)
                                # Check if value two is an int:
                                elif valueTwo.isdigit():
                                    if lookupValueOne['Type'].lower() != 'int':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)

                                # Check if value two is a boolean
                                elif valueTwo == 'true' or valueTwo == 'false':
                                    if lookupValueOne['Type'].lower() != 'bool':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)
                                else:
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                                    
                                
            else:
                if self.current_scope.lookup(condition) == 0:
                    line = ctx.expr().start.line
                    col = ctx.expr().start.column
                    self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para bool: " + condition)
                else:
                    lookupvalue = self.current_scope.lookup(condition)
                    print("Lookupvalue", lookupvalue['Type'].lower())
                    if lookupvalue['Type'].lower() != 'bool' and lookupvalue['Type'].lower() != 'int':
                        line = ctx.expr().start.line
                        col = ctx.expr().start.column
                        self.errors.add(line,col,"Variable asignada no es tipo bool: " + condition)

        # self.popscope()
        # self.current_scope_statement.pop()
    
    def enterWhile_statement(self, ctx: YAPLParser.While_statementContext):
        pass
        # self.current_scope_statement.append("local")
        # self.newscope()

    def exitWhile_statement(self, ctx: YAPLParser.While_statementContext):
        condition = ctx.expr().getText()
        # Check if condition is valid
        if is_valid_boolean_expression(condition):
            pass
        else:
            # Check if its a comparison operation
            if is_valid_comparison_operation(condition):
                if "<" in condition and "<=" not in condition and "=" not in condition:
                    valueOne = condition.split("<")[0]
                    valueTwo = condition.split("<")[1]

                    if valueOne.isdigit() and valueTwo.isdigit():
                        pass
                    else:
                        # Check if value is a valid ID
                        if valueOne.isdigit() == False:
                            if self.current_scope.lookup(valueOne) == 0:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                            else:
                                lookupvalue = self.current_scope.lookup(valueOne)
                                if lookupvalue['Type'].lower() != 'int':
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no es tipo int: " + valueOne)
                                else:
                                    if lookupvalue == 0:
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o el input es invalido: " + valueOne)
                                    

                        if valueTwo.isdigit() == False:
                            if self.current_scope.lookup(valueTwo) == 0:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                            else:
                                lookupvalue = self.current_scope.lookup(valueTwo)
                                if lookupvalue['Type'].lower() != 'int':
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no es tipo int: " + valueTwo)

                elif "<=" in condition:
                    valueOne = condition.split("<=")[0]
                    valueTwo = condition.split("<=")[1]

                    if valueOne.isdigit() and valueTwo.isdigit():
                        pass
                    else:
                        # Check if value is a valid ID
                        if valueOne.isdigit() == False:
                            if self.current_scope.lookup(valueOne) == 0:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                            else:
                                lookupvalue = self.current_scope.lookup(valueOne)
                                if lookupvalue['Type'].lower() != 'int':
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no es tipo int: " + valueOne)

                        if valueTwo.isdigit() == False:
                            if self.current_scope.lookup(valueTwo) == 0:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                            else:
                                lookupvalue = self.current_scope.lookup(valueTwo)
                                if lookupvalue['Type'].lower() != 'int':
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no es tipo int: " + valueTwo)
                                    

                elif "=" in condition:
                    valueOne= condition.split("=")[0]
                    valueTwo = condition.split("=")[1]
                    # Check if they are same type
                    if valueOne.isdigit() and valueTwo.isdigit():
                        pass
                    else:
                        # Check if value is a valid ID
                        lookupValueOne = self.current_scope.lookup(valueOne)
                        lookupValueTwo = self.current_scope.lookup(valueTwo)

                        if lookupValueOne == 0 and lookupValueTwo == 0:

                            # Check if values are strings
                            if valueOne.startswith('"') and valueOne.endswith('"') and valueTwo.startswith('"') and valueTwo.endswith('"'):
                                pass
                            elif valueOne.isdigit() and valueTwo.isdigit():
                                pass    
                            elif valueOne == 'true' or valueOne == 'false' and valueTwo == 'true' or valueTwo == 'false':
                                pass
                            else:
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variables asignadas no existen aun o no son valores validos para comparacion: " + valueOne + "=" + valueTwo)
                        else:
                            print("LookupValueOne", lookupValueOne)
                            print("LookupValueTwo", lookupValueTwo)
                            if lookupValueOne != 0 and lookupValueTwo != 0:
                                # lookupvalue = self.current_scope.lookup(valueOne)
                                if lookupValueOne['Type'].lower() != lookupValueTwo['Type'].lower():
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                            elif lookupValueOne == 0 and lookupValueTwo != 0:
                                # check if value one is a string
                                if valueOne.startswith('"') and valueOne.endswith('"'):
                                    if lookupValueTwo['Type'].lower() != 'string':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                # Check if value one is an int:
                                elif valueOne.isdigit():
                                    if lookupValueTwo['Type'].lower() != 'int':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                
                                # Check if value one is a boolean
                                elif valueOne == 'true' or valueOne == 'false':
                                    if lookupValueTwo['Type'].lower() != 'bool':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                
                                else:
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                            elif lookupValueTwo == 0 and lookupValueOne != 0:
                                # Check if value two is a string
                                if valueTwo.startswith('"') and valueTwo.endswith('"'):
                                    if lookupValueOne['Type'].lower() != 'string':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)
                                # Check if value two is an int:
                                elif valueTwo.isdigit():
                                    if lookupValueOne['Type'].lower() != 'int':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)

                                # Check if value two is a boolean
                                elif valueTwo == 'true' or valueTwo == 'false':
                                    if lookupValueOne['Type'].lower() != 'bool':
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)
                                else:
                                    line = ctx.expr().start.line
                                    col = ctx.expr().start.column
                                    self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                                    
                                
            else:
                if self.current_scope.lookup(condition) == 0:
                    line = ctx.expr().start.line
                    col = ctx.expr().start.column
                    self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para bool: " + condition)
                else:
                    lookupvalue = self.current_scope.lookup(condition)
                    print("Lookupvalue", lookupvalue['Type'].lower())
                    if lookupvalue['Type'].lower() != 'bool' and lookupvalue['Type'].lower() != 'int':
                        line = ctx.expr().start.line
                        col = ctx.expr().start.column
                        self.errors.add(line,col,"Variable asignada no es tipo bool: " + condition)

        # self.popscope()
        # self.current_scope_statement.pop()
    
    def enterLet_declaration(self, ctx: YAPLParser.Let_declarationContext):
        return super().enterLet_declaration(ctx)
    
    def exitLet_declaration(self, ctx: YAPLParser.Let_declarationContext):
        return super().exitLet_declaration(ctx)
    
    def exitExpr(self, ctx: YAPLParser.ExprContext):
        return super().exitExpr(ctx)
    
    def exitVar_assign(self, ctx: YAPLParser.Var_assignContext):
        # Check if variable exists

        copy_global_symbol_table = self.global_symbol_table._symbols.copy()
        for symbol in copy_global_symbol_table:
            # Check if current scope is local
            if self.current_scope_statement[-1] == 'local':
                if symbol['Scope'] == self.current_scope_class:
                    self.current_scope._symbols.append(symbol)

        if self.current_scope.lookup(ctx.ID().getText()) == 0:
            line = ctx.expr().start.line
            col = ctx.expr().start.column
            self.errors.add(line,col,"Variable no existe: " + ctx.ID().getText())
        else:
            variable_declaration = self.current_scope.lookup(ctx.ID())
            variable_type = self.current_scope.lookup(ctx.ID().getText())['Type']
            value = ctx.expr().getText()

            start_with_quote = value.startswith('"')
            end_with_quote = value.endswith('"')
            lookupvalue = self.current_scope.lookup(value)

            # Check if assignment is boolean
            if value == 'true' or value == 'false' or is_valid_comparison_operation(value) or value.isdigit() and variable_type.lower() == self.BOOL.lower():
                if variable_type.lower() != self.BOOL.lower() and variable_type.lower() != self.INT.lower():
                    line = ctx.expr().start.line
                    col = ctx.expr().start.column
                    self.errors.add(line,col,"Variable de tipo: " + self.BOOL + " no puede ser asignada a: " + ctx.ID().getText())

                else:

                    if is_valid_comparison_operation(value):
                        
                        if "<" in value and "<=" not in value and "=" not in value:
                            valueOne = value.split("<")[0]
                            valueTwo = value.split("<")[1]

                            if valueOne.isdigit() and valueTwo.isdigit():
                                pass
                            else:
                                # Check if value is a valid ID
                                if valueOne.isdigit() == False:
                                    if self.current_scope.lookup(valueOne) == 0:
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                                    else:
                                        lookupvalue = self.current_scope.lookup(valueOne)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.expr().start.line
                                            col = ctx.expr().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + valueOne)

                                if valueTwo.isdigit() == False:
                                    if self.current_scope.lookup(valueTwo) == 0:
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                                    else:
                                        lookupvalue = self.current_scope.lookup(valueTwo)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.expr().start.line
                                            col = ctx.expr().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + valueTwo)

                        elif "<=" in value:
                            valueOne = value.split("<=")[0]
                            valueTwo = value.split("<=")[1]

                            if valueOne.isdigit() and valueTwo.isdigit():
                                pass
                            else:
                                # Check if value is a valid ID
                                if valueOne.isdigit() == False:
                                    if self.current_scope.lookup(valueOne) == 0:
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                                    else:
                                        lookupvalue = self.current_scope.lookup(valueOne)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.expr().start.line
                                            col = ctx.expr().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + valueOne)

                                if valueTwo.isdigit() == False:
                                    if self.current_scope.lookup(valueTwo) == 0:
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                                    else:
                                        lookupvalue = self.current_scope.lookup(valueTwo)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.expr().start.line
                                            col = ctx.expr().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + valueTwo)
                                            

                        elif "=" in value:
                            valueOne= value.split("=")[0]
                            valueTwo = value.split("=")[1]
                            # Check if they are same type
                            if valueOne.isdigit() and valueTwo.isdigit():
                                pass
                            else:
                                # Check if value is a valid ID
                                lookupValueOne = self.current_scope.lookup(valueOne)
                                lookupValueTwo = self.current_scope.lookup(valueTwo)

                                if lookupValueOne == 0 and lookupValueTwo == 0:

                                    # Check if values are strings
                                    if valueOne.startswith('"') and valueOne.endswith('"') and valueTwo.startswith('"') and valueTwo.endswith('"'):
                                        pass
                                    elif valueOne.isdigit() and valueTwo.isdigit():
                                        pass    
                                    elif valueOne == 'true' or valueOne == 'false' and valueTwo == 'true' or valueTwo == 'false':
                                        pass
                                    else:
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Variables asignadas no existen aun o no son valores validos para comparacion: " + valueOne + "=" + valueTwo)
                                else:
                                    print("LookupValueOne", lookupValueOne)
                                    print("LookupValueTwo", lookupValueTwo)
                                    if lookupValueOne != 0 and lookupValueTwo != 0:
                                        # lookupvalue = self.current_scope.lookup(valueOne)
                                        if lookupValueOne['Type'].lower() != lookupValueTwo['Type'].lower():
                                            line = ctx.expr().start.line
                                            col = ctx.expr().start.column
                                            self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                    elif lookupValueOne == 0 and lookupValueTwo != 0:
                                        # check if value one is a string
                                        if valueOne.startswith('"') and valueOne.endswith('"'):
                                            if lookupValueTwo['Type'].lower() != 'string':
                                                line = ctx.expr().start.line
                                                col = ctx.expr().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                        # Check if value one is an int:
                                        elif valueOne.isdigit():
                                            if lookupValueTwo['Type'].lower() != 'int':
                                                line = ctx.expr().start.line
                                                col = ctx.expr().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                        
                                        # Check if value one is a boolean
                                        elif valueOne == 'true' or valueOne == 'false':
                                            if lookupValueTwo['Type'].lower() != 'bool':
                                                line = ctx.expr().start.line
                                                col = ctx.expr().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueOne)
                                        
                                        else:
                                            line = ctx.expr().start.line
                                            col = ctx.expr().start.column
                                            self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueOne)
                                    elif lookupValueTwo == 0 and lookupValueOne != 0:
                                        # Check if value two is a string
                                        if valueTwo.startswith('"') and valueTwo.endswith('"'):
                                            if lookupValueOne['Type'].lower() != 'string':
                                                line = ctx.expr().start.line
                                                col = ctx.expr().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)
                                        # Check if value two is an int:
                                        elif valueTwo.isdigit():
                                            if lookupValueOne['Type'].lower() != 'int':
                                                line = ctx.expr().start.line
                                                col = ctx.expr().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)

                                        # Check if value two is a boolean
                                        elif valueTwo == 'true' or valueTwo == 'false':
                                            if lookupValueOne['Type'].lower() != 'bool':
                                                line = ctx.expr().start.line
                                                col = ctx.expr().start.column
                                                self.errors.add(line,col,"Tipo de variable no coincide con la otra: " + valueTwo)
                                        else:
                                            line = ctx.expr().start.line
                                            col = ctx.expr().start.column
                                            self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para comparacion: " + valueTwo)
                                            
                                        
                        
                    else:

                        if value.isdigit():
                            value = int(value)
                            if value < 1:
                                value = False
                            else:
                                value = True
                        
                        if variable_type.lower() == self.INT.lower():
                            if value.lower() == 'true':
                                value = 1
                            elif value.lower() == 'false':
                                value = 0

                        if self.current_scope_statement[-1] == "local" and lookupvalue!=0:
                            self.current_scope.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                            self.global_symbol_table.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                        else:
                            self.current_scope.update(ctx.ID().getText(), value)
                            self.global_symbol_table.update_global(ctx.ID().getText(), value, self.current_scope_statement[-1])


            # Check if assignment is digit
            elif value.isdigit() or variable_type.lower() == self.INT.lower():
                if variable_type.lower() != self.INT.lower() and variable_type.lower() != self.BOOL.lower():
                    line = ctx.expr().start.line
                    col = ctx.expr().start.line
                    self.errors.add(line,col, "Variable de tipo: " + self.INT + " no puede ser asignada a: " + ctx.ID().getText())
                else:
                    if self.current_scope_statement[-1] == "local" and lookupvalue!=0:
                        self.current_scope.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                        self.global_symbol_table.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                    else:
                        self.current_scope.update(ctx.ID().getText(), value)
                        self.global_symbol_table.update_global(ctx.ID().getText(), value, self.current_scope_statement[-1])
            #Check if assignment is string
            elif start_with_quote and end_with_quote:
                if variable_type.lower() != self.STRING.lower():
                    line = ctx.expr().start.line
                    col = ctx.expr().start.column
                    self.errors.add(line,col,"Variable de tipo: " + self.STRING + " no puede ser asignada a: " + ctx.ID().getText())
                else:
                    if self.current_scope_statement[-1] == "local" and lookupvalue!=0:
                        self.current_scope.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                        self.global_symbol_table.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                    else:
                        self.current_scope.update(ctx.ID().getText(), value)
                        self.global_symbol_table.update_global(ctx.ID().getText(), value, self.current_scope_statement[-1])
            # Check if assigned variable is valid
            elif value == self.VOID:
                if self.current_scope_statement[-1] == "local" and lookupvalue!=0:
                    self.current_scope.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                    self.global_symbol_table.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                else:
                    self.current_scope.update(ctx.ID().getText(), value)
                    self.global_symbol_table.update_global(ctx.ID().getText(), value, self.current_scope_statement[-1])
            else:
                # Check for string
                if variable_type.lower() == self.STRING.lower():
                    if self.current_scope.lookup(value) == 0:
                        line = ctx.expr().start.line
                        col = ctx.expr().start.column
                        self.errors.add(line,col,"Variable asignada no definida o valor invalido para tipo string: " + value)
                    else:
                        lookupvalue = self.current_scope.lookup(value)
                        if lookupvalue['Type'].lower() != 'string':
                            line = ctx.expr().start.line
                            col = ctx.expr().start.column
                            self.errors.add(line,col,"Variable asignada no es de tipo string: " + value)
                        else:
                            if self.current_scope_statement[-1] == "local" and lookupvalue!=0:
                                self.current_scope.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                                self.global_symbol_table.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                            else:
                                self.current_scope.update(ctx.ID().getText(), value)
                                self.global_symbol_table.update_global(ctx.ID().getText(), value, self.current_scope_statement[-1])
                # Check for int
                elif variable_type.lower() == self.INT.lower():

                    if "+" in value or "-" in value or "*" in value or "/" in value:
                        if is_valid_arithmethic_expression(value):
                            # Check if value is a valid digit
                            operation_values = re.split(r'[-+*/]', value)
                            operation_values = [operation_values.strip() for operation_values in operation_values if operation_values.strip()]
                            for token in operation_values:
                                if token.isdigit() == False:
                                    if self.current_scope.lookup(token) == 0:
                                        line = ctx.expr().start.line
                                        col = ctx.expr().start.column
                                        self.errors.add(line,col,"Variable asignada no existe aun o no es un valor valido para operacion aritmetica: " + token)
                                    else:
                                        lookupvalue = self.current_scope.lookup(token)
                                        if lookupvalue['Type'].lower() != 'int':
                                            line = ctx.expr().start.line
                                            col = ctx.expr().start.column
                                            self.errors.add(line,col,"Variable asignada no es tipo int: " + token)
                                        else:
                                            if self.current_scope_statement[-1] == "local" and lookupvalue!=0:
                                                self.current_scope.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                                                self.global_symbol_table.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                                            else:
                                                self.current_scope.update(ctx.ID().getText(), value)
                                                self.global_symbol_table.update_global(ctx.ID().getText(), value, self.current_scope_statement[-1])
                            
                        else:
                            line = ctx.type_().start.line
                            col = ctx.type_().start.column
                            self.errors.add(line,col,"Expresion aritmetica invalida: " + value)
                    else:

                        if self.current_scope.lookup(value) == 0:
                            line = ctx.expr().start.line
                            col = ctx.expr().start.column
                            self.errors.add(line,col,"Variable asignada no existe aun: " + value)
                        else:
                            lookupvalue = self.current_scope.lookup(value)
                            if lookupvalue['Type'].lower() != 'int':
                                line = ctx.expr().start.line
                                col = ctx.expr().start.column
                                self.errors.add(line,col,"Variable asignada no es de tipo int: " + value)
                            else:
                                if self.current_scope_statement[-1] == "local" and lookupvalue!=0:
                                    self.current_scope.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                                    self.global_symbol_table.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                                else:
                                    self.current_scope.update(ctx.ID().getText(), value)
                                    self.global_symbol_table.update_global(ctx.ID().getText(), value, self.current_scope_statement[-1])
                
                # Check for bool
                elif variable_type.lower() == self.BOOL.lower():
                    if self.current_scope.lookup(value) == 0:
                        line = ctx.expr().start.line
                        col = ctx.expr().start.column
                        self.errors.add(line,col,"Variable asignada no existe aun: " + value)
                    else:
                        lookupvalue = self.current_scope.lookup(value)
                        if lookupvalue['Type'].lower() != 'bool' and lookupvalue['Type'].lower() != 'int':
                            line = ctx.expr().start.line
                            col = ctx.expr().start.column
                            self.errors.add(line,col,"Variable asignada no es de tipo bool: " + value)
                        else:
                            if self.current_scope_statement[-1] == "local" and lookupvalue!=0:
                                self.current_scope.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                                self.global_symbol_table.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                            else:
                                self.current_scope.update(ctx.ID().getText(), value)
                                self.global_symbol_table.update_global(ctx.ID().getText(), value, self.current_scope_statement[-1])
                        
                # Check for object
                else:
                    if self.current_scope.lookup(value) == 0:
                        line = ctx.expr().start.line
                        col = ctx.expr().start.column
                        self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + value)
                    else:
                        lookupvalue = self.current_scope.lookup(value)
                        if lookupvalue['Type'].lower() != variable_type.lower():
                            line = ctx.expr().start.line
                            col = ctx.expr().start.column
                            self.errors.add(line,col,"Variable asignada no es de tipo: " + variable_type + " :" + value)
                        else:
                            if self.current_scope_statement[-1] == "local" and lookupvalue!=0:
                                self.current_scope.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                                self.global_symbol_table.add(variable_type, ctx.ID().getText(), self.current_scope_statement[-1], value, "Linea: " + str(ctx.expr().start.line) + " Columna: " + str(ctx.expr().start.column), hex(id(ctx.expr())), False, False)
                            else:
                                self.current_scope.update(ctx.ID().getText(), value)
                                self.global_symbol_table.update_global(ctx.ID().getText(), value, self.current_scope_statement[-1])


    def exitReturn_statement(self, ctx: YAPLParser.Return_statementContext):
        self.current_return_values.append(ctx.expr())

    def exitMethod_definition(self, ctx: YAPLParser.Method_definitionContext):

        # for i in self.current_scope._symbols:
        #     print("Before Popping Scopes in scope array:", i)        


        
        current_method_id = self.method_table._methods[-1]['ID']
        self.method_table._methods[-1]['size'] = self.current_scope.getsize()
        # print('Current method_table', self.method_table._methods)
        self.global_method_table.update(current_method_id, self.method_table._methods[-1])

        self.popscope(merging=True)
        self.current_scope_statement.pop()

        type = ctx.type_().getText()
        try:
            return_expr_ctx = self.current_return_values.pop()
            return_value = return_expr_ctx.getText()
        except:
            return_expr_ctx = ""
            return_value = ""
            line = ctx.type_().start.line
            col = ctx.type_().start.column
            self.errors.add(line,col,"Metodo no tiene return: " + ctx.ID().getText())
            return

        # print("Current_scope", self.current_scope._symbols)

        # print("Return-value", return_expr_ctx.getText())

        if type.lower() == self.VOID.lower():
            if return_value.lower() != self.VOID.lower():
                line = return_expr_ctx.start.line
                col = return_expr_ctx.start.column
                self.errors.add(line,col,"Metodo tipo void no puede retornar un valor: " + return_value)
        elif type.lower() == self.STRING.lower():
            if return_value.startswith('"') and return_value.endswith('"'):
                pass
            else:
                # Check if return value is a valid ID
                if self.current_scope.lookup(return_value) == 0:
                    line = return_expr_ctx.start.line
                    col = return_expr_ctx.start.column
                    self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + return_value)
                else:
                    lookupvalue = self.current_scope.lookup(return_value)
                    if lookupvalue['Type'].lower() != 'string':
                        line = return_expr_ctx.start.line
                        col = return_expr_ctx.start.column
                        self.errors.add(line,col,"Variable asignada no es de tipo string: " + return_value)
        elif type.lower() == self.INT.lower():
            if return_value.isdigit():
                pass
            else:
                # Check if return value is a valid ID
                # print("Return value", return_value)
                # print("Current scope", self.current_scope._symbols)
                if self.current_scope.lookup(return_value) == 0:
                    line = return_expr_ctx.start.line
                    col = return_expr_ctx.start.column
                    self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + return_value)
                else:
                    lookupvalue = self.current_scope.lookup(return_value)
                    if lookupvalue['Type'].lower() != 'int':
                        line = return_expr_ctx.start.line
                        col = return_expr_ctx.start.column
                        self.errors.add(line,col,"Variable asignada no es de tipo int: " + return_value)
        elif type.lower() == self.BOOL.lower():
            if return_value == 'true' or return_value == 'false':
                pass    
            else:
                # Check if return value is a valid ID
                if self.current_scope.lookup(return_value) == 0:
                    line = return_expr_ctx.start.line
                    col = return_expr_ctx.start.column
                    self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + return_value)
                else:
                    lookupvalue = self.current_scope.lookup(return_value)
                    if lookupvalue['Type'].lower() != 'bool':
                        line = return_expr_ctx.start.line
                        col = return_expr_ctx.start.column
                        self.errors.add(line,col,"Variable asignada no es de tipo bool: " + return_value)
        else: # Check if type is a valid class
            if self.class_table.lookup(type) == 0 and type.lower() != self.IO.lower() and type.lower() != "self_type":
                line = ctx.type_().start.line
                col = ctx.type_().start.column
                self.errors.add(line,col,"Tipo especificado no existe: " + type)
            else:
                if return_value.lower() == self.VOID.lower():
                    pass
                else:
                    # Check if return value is a valid ID
                    if self.current_scope.lookup(return_value) == 0:
                        line = return_expr_ctx.start.line
                        col = return_expr_ctx.start.column
                        self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + return_value)
                    else:
                        lookupvalue = self.current_scope.lookup(return_value)
                        if lookupvalue['Type'].lower() != type.lower():
                            line = return_expr_ctx.start.line
                            col = return_expr_ctx.start.column
                            self.errors.add(line,col,"Variable asignada no es de tipo: " + type + " :" + return_value)



        # print("Exited method definition", self.current_scope._symbols)
    
    def enterSimple_method_definition(self, ctx: YAPLParser.Simple_method_definitionContext):
        # self.current_scope_statement = "local"

        copy_global_symbol_table = self.global_symbol_table._symbols.copy()
        for symbol in copy_global_symbol_table:
            # Check if current scope is local
            if self.current_scope_statement[-1] == 'local':
                if symbol['Scope'] == self.current_scope_class:
                    self.current_scope._symbols.append(symbol)

        function_call_id = None
        variable_name = None
        variable_type = None

        # Check if ctx.ID is array or not

        if len(ctx.ID()) > 1:
            variable_name = ctx.ID()[0].getText()
            function_call_id = ctx.ID()[1].getText()
        else:
            function_call_id = ctx.ID()[0].getText()

        # Check if variable exists
        if variable_name is not None:
            if self.current_scope.lookup(variable_name) == 0 and self.default_methods.lookup(variable_name) == 0:
                if variable_name != 'main':
                    line = ctx.start.line
                    col = ctx.start.column
                    # print('self.current_scope.lookup(variable_name)', self.current_scope._symbols)
                    self.errors.add(line,col,"Variable de la llamada no existe: " + variable_name + '.' + function_call_id + '()')
            else:
                variable_type = self.current_scope.lookup(variable_name)['Type']     



        address = hex(id(ctx))
        parameters = []
        position = "Linea: " + str(ctx.start.line) + " Columna: " + str(ctx.start.column)

        parameter_list = ctx.expr()
        for parameter in parameter_list:
            parameters.append(parameter.getText())
        
        # Check if number of parameters is the same
        method = self.global_method_table.lookup_w_class(function_call_id, variable_type)
        local_method = self.method_table.lookup(function_call_id)
        # Get types of method's parameters
        parameters_type = []
        if method != 0:
            for parameter in method['Parameters']:
                parameters_type.append(parameter.split(":")[1])
        elif local_method != 0 and variable_name is None:
            for parameter in local_method['Parameters']:
                parameters_type.append(parameter.split(":")[1])
            method = local_method
            variable_name = ""

        # if function_call_id == 'pruebarde':
        #     print('----------------debug print-------------')
        #     print('function_call_id', function_call_id)
        #     print('variable_name', variable_name)
        #     print('variable_type', variable_type)
        #     print('parameters', parameters)
        #     print('method', method)
        #     print('local', local_method)

        
        
        default_method = self.default_methods.lookup(function_call_id)
        if method != 0:
            if len(method['Parameters']) != len(parameters):
                # print('Lenes', len(method['Parameters']), len(parameters))
                line = ctx.start.line
                col = ctx.start.column
                self.errors.add(line,col,"Numero de parametros no coincide con la declaracion: " + variable_name + '.' + function_call_id + '()')
            else: # Check if parameter types are the same
                count = 0 # Counter for the parameters in the method call
                for param_type in parameters_type:
                    if param_type == self.STRING:
                        # Check if parameter is a string
                        if parameters[count].startswith('"') and parameters[count].endswith('"'):
                            pass # Valid string literal
                        else:
                            # Check if parameter is a valid ID
                            if self.current_scope.lookup(parameters[count]) == 0:
                                line = ctx.start.line
                                col = ctx.start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + parameters[count])
                            else:
                                lookupvalue = self.current_scope.lookup(parameters[count])
                                if lookupvalue['Type'].lower() != 'string':
                                    line = ctx.start.line
                                    col = ctx.start.column
                                    self.errors.add(line,col,"Variable asignada no es de tipo string: " + parameters[count])
                    elif param_type == self.INT:
                        # Check if parameter is a digit
                        if parameters[count].isdigit():
                            pass # Valid digit
                        else:
                            # Check if parameter is a valid ID
                            if self.current_scope.lookup(parameters[count]) == 0:
                                line = ctx.start.line
                                col = ctx.start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + parameters[count])
                            else:
                                lookupvalue = self.current_scope.lookup(parameters[count])
                                if lookupvalue['Type'].lower() != 'int':
                                    line = ctx.start.line
                                    col = ctx.start.column
                                    self.errors.add(line,col,"Variable asignada no es de tipo int: " + parameters[count])
                    elif param_type == self.BOOL:
                        # Check if parameter is a boolean
                        if parameters[count] == 'true' or parameters[count] == 'false':
                            pass
                        else:
                            # Check if parameter is a valid ID
                            if self.current_scope.lookup(parameters[count]) == 0:
                                line = ctx.start.line
                                col = ctx.start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + parameters[count])
                            else:
                                lookupvalue = self.current_scope.lookup(parameters[count])
                                if lookupvalue['Type'].lower() != 'bool':
                                    line = ctx.start.line
                                    col = ctx.start.column
                                    self.errors.add(line,col,"Variable asignada no es de tipo bool: " + parameters[count])
                    else: # Cuando el tipo no es basico
                        # Check if parameter is a valid ID
                        if self.current_scope.lookup(parameters[count]) == 0:
                            line = ctx.start.line
                            col = ctx.start.column
                            self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + parameters[count])
                        else:
                            lookupvalue = self.current_scope.lookup(parameters[count])
                            if lookupvalue['Type'].lower() != param_type.lower():
                                line = ctx.start.line
                                col = ctx.start.column
                                self.errors.add(line,col,"Variable asignada no es de tipo: " + param_type + " :" + parameters[count])

                    count += 1
                    

        else:

            parameters_type = []
            if default_method != 0:
                for parameter in default_method['Parameters']:
                    parameters_type.append(parameter.split(":")[1])

            if default_method != 0:
                if len(default_method['Parameters']) != len(parameters):
                    line = ctx.start.line
                    col = ctx.start.column
                    self.errors.add(line,col,"Numero de parametros no coincide con la declaracion: " + variable_name + '.' + function_call_id + '()')
                else: # Check if parameter types are the same
                    count = 0 # Counter for the parameters in the method call
                    for param_type in parameters_type:
                        if param_type == self.STRING:
                            # Check if parameter is a string
                            if parameters[count].startswith('"') and parameters[count].endswith('"'):
                                pass
                            else:
                                # Check if parameter is a valid ID
                                if self.current_scope.lookup(parameters[count]) == 0:
                                    line = ctx.start.line
                                    col = ctx.start.column
                                    self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + parameters[count])
                                else:
                                    lookupvalue = self.current_scope.lookup(parameters[count])
                                    if lookupvalue['Type'].lower() != 'string':
                                        line = ctx.start.line
                                        col = ctx.start.column
                                        self.errors.add(line,col,"Variable asignada no es de tipo string: " + parameters[count])
                        elif param_type == self.INT:
                            # Check if parameter is a digit
                            if parameters[count].isdigit():
                                pass
                            else:
                                # Check if parameter is a valid ID
                                if self.current_scope.lookup(parameters[count]) == 0:
                                    line = ctx.start.line
                                    col = ctx.start.column
                                    self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + parameters[count])
                                else:
                                    lookupvalue = self.current_scope.lookup(parameters[count])
                                    if lookupvalue['Type'].lower() != 'int':
                                        line = ctx.start.line
                                        col = ctx.start.column
                                        self.errors.add(line,col,"Variable asignada no es de tipo int: " + parameters[count])
                        elif param_type == self.BOOL:
                            # Check if parameter is a boolean
                            if parameters[count] == 'true' or parameters[count] == 'false':
                                pass
                            else:
                                # Check if parameter is a valid ID
                                if self.current_scope.lookup(parameters[count]) == 0:
                                    line = ctx.start.line
                                    col = ctx.start.column
                                    self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + parameters[count])
                                else:
                                    lookupvalue = self.current_scope.lookup(parameters[count])
                                    if lookupvalue['Type'].lower() != 'bool':
                                        line = ctx.start.line
                                        col = ctx.start.column
                                        self.errors.add(line,col,"Variable asignada no es de tipo bool: " + parameters[count])
                        else: # Cuando el tipo no es basico
                            # Check if parameter is a valid ID
                            if self.current_scope.lookup(parameters[count]) == 0:
                                line = ctx.start.line
                                col = ctx.start.column
                                self.errors.add(line,col,"Variable asignada no existe aun o no es un input valido: " + parameters[count])
                            else:
                                lookupvalue = self.current_scope.lookup(parameters[count])
                                if lookupvalue['Type'].lower() != param_type.lower():
                                    line = ctx.start.line
                                    col = ctx.start.column
                                    self.errors.add(line,col,"Variable asignada no es de tipo: " + param_type + " :" + parameters[count])

                        count += 1

        # Check if method has already called init()
        if function_call_id == 'init':
            lookupmethod = self.method_call_table.lookup(variable_name)
            if lookupmethod != 0 and lookupmethod['Function_ID'] == 'init' and lookupmethod['ID'] == variable_name:
                line = ctx.start.line
                col = ctx.start.column
                self.errors.add(line,col,"Metodo init() ya ha sido llamado")

        #Check if method calls another method before init()
        if function_call_id != 'init':
            lookupmethod = self.method_call_table.lookup(variable_name)
            lookupdefaultmethod = self.default_methods.lookup(function_call_id)
            print('variable_name', variable_name)

            if lookupdefaultmethod !=0:
                pass # No hacer nada porque es valido no llamar a init en este caso
            elif lookupmethod == 0 and variable_name != 'main' and self.current_scope_statement[-1] != 'local':
                line = ctx.start.line
                col = ctx.start.column
                self.errors.add(line,col,"Metodo init() debe ser llamado primero")

        # Check if method exists
        if function_call_id is not None:
            if variable_type is not None:
                method = self.global_method_table.lookup_w_class(function_call_id, variable_type)
                if variable_type.lower() not in self.default_data_types:
                    if method == 0:
                        line = ctx.start.line
                        col = ctx.start.column
                        self.errors.add(line,col,"Metodo no existe: " + variable_name + '.' + function_call_id + '()')
                else:
                    default_methods = self.default_methods.lookup_w_class(function_call_id, variable_type)
                    if default_methods == 0:
                        line = ctx.start.line
                        col = ctx.start.column
                        self.errors.add(line,col,"Metodo no existe: " + variable_name + '.' + function_call_id + '()')
            else:
                method = self.global_method_table.lookup(function_call_id)
                default_methods = self.default_methods.lookup(function_call_id)
                if method == 0 and default_methods == 0:
                    line = ctx.start.line
                    col = ctx.start.column
                    self.errors.add(line,col,"Metodo no existe: " + function_call_id + '()')


        if self.method_call_table.lookup(function_call_id) == 0:
            self.global_method_call_table.add(variable_type, variable_name, function_call_id, parameters, self.current_scope_statement[-1], address, position)
            self.method_call_table.add(variable_type, variable_name, function_call_id, parameters, self.current_scope_statement[-1], address, position)
        else:
            line = ctx.start.line
            col = ctx.start.column
            self.errors.add(line, col, "Metodo duplicado: " + function_call_id)

        



    def exitSimple_method_definition(self, ctx: YAPLParser.Simple_method_definitionContext):
        # self.method_call_table = MethodCallTable()

        variable_name = None

        # Check if ctx.ID is array or not
        if type(ctx.ID()) is TerminalNode:
            method_id = ctx.ID().getText()
        else:
            if len(ctx.ID()) > 1:
                variable_name = ctx.ID()[0].getText()
                method_id = ctx.ID()[1].getText()
            else:
                method_id = ctx.ID()[0].getText()

        # Get current type of variable
        variable_lookup = self.current_scope.lookup(variable_name)
        if type(variable_lookup) is not int:
            variable_type = self.current_scope.lookup(variable_name)['Type']

            # Get if method exists
            method = self.global_method_table.lookup_w_class(method_id, variable_type)
            if variable_type.lower() not in self.default_data_types:
                if method == 0:
                    line = ctx.start.line
                    col = ctx.start.column
                    self.errors.add(line,col,"Metodo no existe: " + method_id + " en clase: " + variable_type)
            else:
                default_methods = self.default_methods.lookup_w_class(method_id, variable_type)
                if default_methods == 0:
                    line = ctx.start.line
                    col = ctx.start.column
                    self.errors.add(line,col,"Metodo no existe: " + method_id + " para tipo: " + variable_type)
            
        

    def exitClas_list(self, ctx: YAPLParser.Clas_listContext):
        class_type = ctx.type_()[0].getText()
        line = ctx.type_()[0].start.line
        col = ctx.type_()[0].start.column

        # Verificar que haya un metodo main en clase main sin parametros
        if class_type.lower() == 'main':
            main_method = self.method_table.lookup("main")
            if main_method == 0:
                self.errors.add(line,col,"No se encontro metodo main")
            else:
                if len(main_method['Parameters']) > 0:
                    line = main_method['Position'].split(" ")[1]
                    col = main_method['Position'].split(" ")[3]
                    self.errors.add(line,col,"Metodo main no puede tener parametros")

        if class_type.lower() in self.default_data_types:
            self.errors.add(line,col,"Clase no puede ser tipo basico: " + class_type)


        self.method_table = MethodTable()


        self.popscope()
        self.current_scope_statement.pop()
        print('Saliendo de la clase: ' + class_type)

        # print('Clases actuales: ', self.class_table._classes)
        # print('scope', self.current_scope._symbols)
        for variables in self.current_scope._symbols:
            if variables['Scope'] == f'global -> {class_type}':
                self.class_table._classes[-1]['size'] = variables['size']
        
        for methods in self.global_method_table._methods:
            if methods['Scope'] == f'global -> {class_type}':
                self.class_table._classes[-1]['size'] += methods['size']

        if class_type == self.VOID:
            self.node_type[ctx] = self.ERROR
            self.errors.add(line, col, "Clase no puede ser tipo void")
            return
        
        

    def exitProgram(self, ctx: YAPLParser.ProgramContext):
        main_class = self.class_table.lookup("main")
        if main_class == 0: # Error si no hay clase main
            self.errors.add(0,0,"No se encontro clase main")

        for i in self.class_table._classes:
            if i['Inheritance'] is not None:
                if self.class_table.lookup(i['Inheritance']) == 0:

                    # Check if it is basic data type
                    if i['Inheritance'].lower() in self.basic_data_type:
                        line = i['Position'].split(" ")[1]
                        col = i['Position'].split(" ")[3]
                        self.errors.add(line,col,"Clase heredada no puede ser tipo basico: " + i['Inheritance'])
                    else:
                        line = i['Position'].split(" ")[1]
                        col = i['Position'].split(" ")[3]
                        self.errors.add(line,col,"Clase heredada no existe: " + i['Inheritance'])

        self.current_scope.totable()
        print(" --- FIN PROGRAMA --- ")

        print("\n --- Resumen de tablas --- ")
        self.class_table.totable()
        self.global_method_table.totable()
        print(" --- Llamadas a metodos --- ")
        self.global_method_call_table.totable()
        print(" --- Tabla de simbolos (Todos los simbolos) --- ")
        self.global_symbol_table.totable()

        if len(self.errors.GetErrores()) > 0:
            print(" --- ERRORES --- ")
            print(self.errors.GetErrores())


def is_valid_arithmethic_expression(input_str): # Receives string
    # Define a regular expression pattern to match valid arithmetic operations
    pattern = r'^\s*((\d+|\w+)\s*([-+*/])\s*(\d+|\w+))*\s*$'

    # Use re.match to check if the input string matches the pattern
    match = re.match(pattern, input_str)

    # If there's a match and it covers the entire string, it's a valid arithmetic operation
    if match and match.group(0) == input_str:
        return True
    else:
        return False

def is_valid_boolean_expression(expression):
    if expression == 'true' or expression == 'false':
        return True
    else:
        return False

def is_valid_comparison_operation(input_str):
    # Define a regular expression pattern to match valid comparison operations
    pattern = r'^\s*(\w+)\s*(<|<=|=)\s*(\w+)\s*$'

    # Use re.match to check if the input string matches the pattern
    match = re.match(pattern, input_str)

    # If there's a match and it covers the entire string, it's a valid comparison operation
    if match and match.group(0) == input_str:
        return True
    else:
        return False
    
def is_unary_expression(expression):
    if expression.startswith('not') or expression.startswith('~'):
        return True
    else:
        return False

