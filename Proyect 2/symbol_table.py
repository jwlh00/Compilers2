from prettytable import PrettyTable

class SymbolTable():
    def __init__(self) -> None:
        self.pretty_table = PrettyTable()
        self._symbols = []
        print('Iniciando nuevo ambito/scope')
    
    def add(self, type, id, scope, value, position, address, isParameter, isInherited, class_table = None):
        size = 0
        if type.lower() == 'int':
            size = 4
        elif type.lower() == 'string':
            if value.startswith('"') or value.startswith("'") and value.endswith('"') or value.endswith("'"):
                size = 4 * len(value.strip('"').strip("'"))
            else:
                size = 4
        elif type.lower() == 'bool':
            size = 1
        else:
            if class_table:
                _class = class_table.lookup(type)
                if _class:
                    size = _class['size']
                else:
                    size = 0
            else:
                size = 0

        self._symbols.append({
            'Type': type,
            'ID': id,
            'Scope': scope,
            'Value': value,
            'Position': position,
            'Address': address,
            'IsParameter': isParameter,
            'IsInherited': isInherited,
            'size': size
        })
    
    def lookup(self, id):
        symbols_copy = self._symbols.copy()
        symbols_copy.reverse()
        for symbol in symbols_copy:
            if symbol['ID'] == id:
                return symbol
        return 0
    
    def lookup_w_type(self, id, type):
        symbols_copy = self._symbols.copy()
        symbols_copy.reverse()
        for symbol in symbols_copy:
            if '->' in type and len(symbol['Scope'].split('->')) > 1:
                type = type.split('->')[1].strip()
                scope = symbol['Scope'].split('->')[1].strip()
                if symbol['ID'] == id and scope == type:
                    return symbol
        return 0

    def getsize(self):
        cacheID = set()
        cacheScope = set()
        total_size = 0
        for symbol in self._symbols:
            if symbol['ID'] not in cacheID or symbol['Scope'] not in cacheScope:
                # print(symbol['ID'] + ' = ' + symbol['Scope'])
                # print(symbol['size'])
                cacheID.add(symbol['ID'])
                cacheScope.add(symbol['Scope'])
                total_size += symbol['size']
        return total_size
    
    def totable(self):
        self.pretty_table.field_names = ['Type', 'ID', 'Scope', 'Value','Position', 'Address', 'IsParameter', 'IsInherited', 'size']
        for i in self._symbols:
            self.pretty_table.add_row(list(i.values()))

        print(" -- Simbolos -- ")
        print(self.pretty_table)
        self.pretty_table.clear_rows()

    # Delete certain symbols from the table
    def delete(self, ID):
        for symbol in self._symbols:
            if symbol['ID'] == ID:
                self._symbols.remove(symbol)

    # Update the value of a symbol
    def update(self, ID, value):
        for symbol in self._symbols:
            if symbol['ID'] == ID:
                symbol['Value'] = value
                if symbol['Type'].lower() =='string':
                    if value.startswith('"') or value.startswith("'") and value.endswith('"') or value.endswith("'"):
                        symbol['size'] = 4 * len(value.strip('"').strip("'"))
                    else:
                        symbol['size'] = 4
                elif symbol['Type'].lower() =='int':
                    symbol['size'] = 4
                elif symbol['Type'].lower() =='bool':
                    symbol['size'] = 1
    
    def update_global(self, ID, value, scope):
        for symbol in self._symbols:
            if symbol['ID'] == ID and symbol['Scope'] == scope:
                symbol['Value'] = value
                if symbol['Type'].lower() =='string':
                    if value.startswith('"') or value.startswith("'") and value.endswith('"') or value.endswith("'"):
                        symbol['size'] = 4 * len(value.strip('"').strip("'"))
                    else:
                        symbol['size'] = 4
                elif symbol['Type'].lower() =='int':
                    symbol['size'] = 4
                elif symbol['Type'].lower() =='bool':
                    symbol['size'] = 1

class ClassTable():
    def __init__(self) -> None:
        self.pretty_table = PrettyTable()
        self._classes = []
        print(" -- Iniciando nuevo ambito/scope -- ")
    def add(self,type, id, scope, position, inheritance, address, size=0):
        self._classes.append({
            'Type': type,
            'ID': id,
            'Scope': scope,
            'Inheritance': inheritance,
            'Position': position,
            'Memory Address': address,
            'size': size
        })
    def lookup(self, type):
        for _class in self._classes:
            if _class['Type'] == type:
                return _class
        return 0
    
    def totable(self):
        self.pretty_table.field_names = ['Type', 'ID', 'Scope', 'Inheritance', 'Position', 'Memory Address', 'size']
        for i in self._classes:
            self.pretty_table.add_row(list(i.values()))

        print(" -- Clases -- ")
        print(self.pretty_table)
        self.pretty_table.clear_rows()


class MethodTable():

    def __init__(self) -> None:
        self.pretty_table = PrettyTable()
        self._methods = []
        print(" -- Iniciando nuevo ambito/scope -- ")

    def add(self, type, id, parameters, scope, address, position, isInherited = False, size = 0):
        self._methods.append({
            'Type': type,
            'ID': id,
            'Parameters': parameters,
            'Scope': scope,
            'Address': address,
            'Position': position,
            'IsInherited': isInherited,
            'size': size
        })
    
    def lookup(self, variable):
        for method in self._methods:
            if method['ID'] == variable:
                return method
        return 0
    
    def lookup_w_class(self, id, type):
        for method in self._methods:
            try:
                method_scope = method['Scope'].split('->')[1].strip()
            except:
                method_scope = 'local'
            if method['ID'] == id and method_scope == type:
                return method
        
        return 0

    def delete(self, ID):
        for method in self._methods:
            if method['ID'] == ID:
                self._methods.remove(method)        
    
    def totable(self):
        self.pretty_table.field_names = ['Type', 'ID', 'Parameters', 'Scope', 'Address', 'Position', 'IsInherited', 'size']
        for i in self._methods:
            self.pretty_table.add_row(list(i.values()))

        print(" -- Metodos -- ")
        print(self.pretty_table)
        self.pretty_table.clear_rows()

    def update(self, ID, method_table):
        for method in self._methods:
            if method['ID'] == ID and method['Scope'] == method_table['Scope']:
                # print('Updating method: ' + method['ID'] + ' in scope: ' + method['Scope'])
                # print('size: ' + str(method_table['size']))
                method['Parameters'] = method_table['Parameters']
                method['Scope'] = method_table['Scope']
                method['Address'] = method_table['Address']
                method['Position'] = method_table['Position']
                method['IsInherited'] = method_table['IsInherited']
                method['size'] = method_table['size']

class MethodCallTable():
    def __init__(self) -> None:
        self.pretty_table = PrettyTable()
        self._methods = []
        print(" -- Iniciando nuevo ambito/scope -- ")

    def add(self, type, id, function_id, parameters, scope, address, position):
        self._methods.append({
            'Type': type,
            'ID': id,
            'Function_ID': function_id,
            'Parameters': parameters,
            'Scope': scope,
            'Address': address,
            'Position': position
        })
    
    def lookup(self, variable):
        for method in self._methods:
            if method['ID'] == variable:
                return method
        return 0
    
    def lookup_w_class(self, variable, class_name):
        for method in self._methods:
            try:
                method_scope = method['Scope'].split('->')[1].strip()
            except:
                method_scope = 'local'
            if method['ID'] == variable and method_scope == class_name:
                return method
        
        return 0
    
    def totable(self):
        self.pretty_table.field_names = ['Type', 'ID', 'Function_ID', 'Parameters', 'Scope', 'Address', 'Position']
        for i in self._methods:
            self.pretty_table.add_row(list(i.values()))

        print(" -- Metodos -- ")
        print(self.pretty_table)
        self.pretty_table.clear_rows()


class SemanticError():
    def __init__(self) -> None:
        self._errors = []
        # self.IDENTIFICADOR_DECLARADO_MULTIPLES_VECES = 'El identificador ya fue declarado'
        # self.PARAMETROS_INCORRECTOS_METODO = 'Los parametros del metodo no coinciden'
        # self.TIPO_INCORRECTO = 'El tipo de dato del parametro no coincide'
        # self.EQ_OPS = 'El tipo de datos de operandos no es el mismo para los operadores de igualacion'
        # self.ARITH_OP = 'El tipo de dato de operando debe ser INT para operadores aritméticos.'
        # self.REL_OP = 'El tipo de dato de operando debe ser INT para operadores de relación.'
        # self.COND_OP = 'El tipo de dato en operación condicional debe ser boolean.'
        # self.IF_BOOLEAN = 'El tipo de dato dentro de condición de IF debe ser boolean.'
        # self.WHILE_BOOLEAN = 'El tipo de dato dentro de condición de WHILE debe ser boolean.'
        # self.ASIGNACION = 'La asignación de dos valores deben ser del mismo tipo.'
        # self.RETURN_TYPE = 'El valor de retorno debe de ser del mismo tipo con que fue declarado el método.'
        # self.METHOD_NOT_DECLARED = 'El método no existe o no hay definición del método previamente a ser invocado.'

    
    def add(self, line, col, msg):
        self._errors.append({
            'Line': line,
            'Column': col,
            'Description': msg
        })

    def ToString(self):
        for error in self._errors:
            print(' => Line ' + str(error['Line']) + ':' + str(error['Column']) + ' ' + error['Description'])

    def GetErrores(self):
        errors = []
        for error in self._errors:
            errors.append(' => Line ' + str(error['Line']) + ':' + str(error['Column']) + ' ' + error['Description'])
        return errors