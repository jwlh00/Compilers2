import os
from antlr4 import *
from symbol_table import *
from YAPLLexer import *
from YAPLParser import *
from antlr4.tree.Tree import TerminalNodeImpl

class YAPLPrinter():
    def __init__(self, input_file):
        self.input = input_file
        self.input_stream = FileStream(self.input)
        self.lexer = YAPLLexer(self.input_stream)
        self.token_stream = CommonTokenStream(self.lexer)
        self.parser = YAPLParser(self.token_stream)
        self.error_listener = MyErrorListener() # Sintaxis .errors
        self.parser.removeErrorListeners()
        self.parser.addErrorListener(self.error_listener)
        self.tree = self.parser.program()
        self.treeStruct = None
        self.lexicalErrors = [] # Lexico
        self.symbolTable = SymbolTable()
        self.semanticAnalyzer = None # Semantico .errors
        self.tokens = {}
        self.lexicalAnalysis()
        self.syntacticAnalysis()
        self.semanticAnalysis()
    
    def lexicalAnalysis(self):
        nonErrors, lexicalErrors = self.get_tokens()

        if lexicalErrors:
            print("\nTokens Found:")
            for token in nonErrors:
                print(token)
            print("\nErrores Found:")
            for error in lexicalErrors:
                print(error)
            # print()
        else:
            print("\nTokens Found:")
            for token in nonErrors:
                print(token)
            print()

    def syntacticAnalysis(self):
        if self.error_listener.errors:
            print("\nERRORES SINTÁCTICOS IDENTIFICADOS:")
            for error in self.error_listener.errors:
                print(error)
        # else:

        root = self.build_tree(self.tree)
        self.treeStruct = AbstractTree()
        self.traverse_tree(root, self.treeStruct)

        self.treeStruct.root = self.treeStruct.nodes[0]

        classProperties = {}
        className = ""

        classProperties["IO"] = ["out_string", "out_int", "in_string", "in_int"]

        self.symbolTable.insert(Symbol("IO", "Class", "Class", None, None, "global", -1))
        self.symbolTable.insert(Symbol("String", "Class", "Class", None, None, "global", -1))
        self.symbolTable.insert(Symbol("Int", "Class", "Class", None, None, "global", -1))
        self.symbolTable.insert(Symbol("Bool", "Class", "Class", None, None, "global", -1))
        
        # llenar diccionario de clases y sus propiedades
        for node in self.treeStruct.nodes:
            if isinstance(node, AbstractTreeNode):
                rule_name = node.val

                if rule_name == "classDefine":
                    className = node.children[1].val
                    classProperties[className] = []

                if rule_name == "property":
                    classProperties[className].append(node.children[0].children[0].val)
                
                if rule_name == "method":
                    classProperties[className].append(node.children[0].val)
        
        global_scope = "global"
        class_scope = ""
        method_scope = ""
        current_scope = global_scope

        #iteramos los nodos del arbol y llenamos la tabla de simbolos
        for node in self.treeStruct.nodes:
            # print(node)
            if isinstance(node, AbstractTreeNode):
                rule_name = node.val
                
                if rule_name == "classDefine":
                    current_scope = global_scope
                    # print(node)
                    class_name = node.children[1].val
                    if node.children[2].val == "inherits":
                        inherits_name = node.children[3].val
                        self.symbolTable.insert(Symbol(class_name, "Class", "Class", None, inherits_name, current_scope, node.line))
                    else:
                        self.symbolTable.insert(Symbol(class_name, "Class", "Class", None, None, current_scope, node.line))
                    class_scope = class_name
                    current_scope = class_name
                    method_scope = ""
                elif rule_name == "method":
                    current_scope = class_scope
                    method_name = node.children[0].val
                    method_type = self.extract_method_return_type(node)
                    self.symbolTable.insert(Symbol(method_name, "Method", method_type, None, None, current_scope, node.line))
                    method_scope = method_name
                    current_scope = method_name
                elif rule_name == "property":
                    if len(node.children) > 1: # es una asignacion
                        current_scope = method_scope if method_scope != "" else class_scope
                        childFormal = node.children[0]
                        childExpr = node.children[2]
                        var_name = childFormal.children[0].val
                        var_type = childFormal.children[2].val
                        var_value = childExpr.children[0].val
                        self.symbolTable.insert(Symbol(var_name, "Variable", var_type, var_value, None, class_scope, node.line))
                    else: # solo es una declaracion
                        current_scope = method_scope if method_scope != "" else class_scope
                        childFormal = node.children[0]
                        var_name = childFormal.children[0].val
                        var_type = childFormal.children[2].val
                        self.symbolTable.insert(Symbol(var_name, "Variable", var_type, None, None, class_scope, node.line))
                elif rule_name == "varDeclaration":
                    current_scope = method_scope if method_scope != "" else class_scope
                    childExpr = node.children[2]
                    var_name = node.children[0].val
                    if len(childExpr.children) == 1:
                        var_value = childExpr.children[0].val
                    else:
                        var_value = self.getExprChildren(childExpr)

                    matching_formal_symbol = None
                    for symbol in self.symbolTable.symbols:
                        if symbol.name == var_name and symbol.id_type == "Variable" and (symbol.scope.split(".")[0] == class_scope or symbol.scope.split(".")[0] == method_scope):
                            matching_formal_symbol = symbol
                            break 
                    if matching_formal_symbol is None:
                        for symbol in self.symbolTable.symbols:
                            if symbol.name == var_name and symbol.id_type == "Variable":
                                matching_formal_symbol = symbol
                                break 
                        if matching_formal_symbol is None:
                            self.symbolTable.insert(Symbol(var_name, "Variable", "Void", var_value, None, class_scope + "." + current_scope, node.line))
                        else:
                            self.symbolTable.insert(Symbol(var_name, "Variable", matching_formal_symbol.data_type, var_value, matching_formal_symbol.scope, class_scope + "." + current_scope, node.line))

                    else:
                        if "not" in var_value:
                            variable_origina_simbolo = self.symbolTable.lookup_all(var_name)
                            if variable_origina_simbolo.value == "true":
                                self.symbolTable.update_symbol_value(var_name, "false")
                                self.symbolTable.update_symbol_line(var_name, node.line)
                            else:
                                self.symbolTable.update_symbol_value(var_name, "true")
                                self.symbolTable.update_symbol_line(var_name, node.line)
                        else:
                            self.symbolTable.update_symbol_value(var_name, var_value)
                            self.symbolTable.update_symbol_line(var_name, node.line)
                    
                elif rule_name == "formal" and node.parent.val != "property":
                    current_scope = method_scope if method_scope != "" else class_scope
                    var_name = node.children[0].val
                    var_type = node.children[2].val
                    self.symbolTable.insert(Symbol(var_name, "Parameter", var_type, None, None, class_scope +"."+ current_scope, node.line))

                elif rule_name == "expr" and len(node.children) == 3 and node.children[1].val == "(" and node.children[2].val == ")":
                    method_call_name = node.children[0].val
                    self.symbolTable.insert(Symbol(method_call_name, "MethodCall", "Void", self.getExprChildren(node.children[2]), None, class_scope + "." + method_scope, node.line))

                elif rule_name == "expr" and len(node.children) == 4 and node.children[1].val == "(" and node.children[3].val == ")":
                    procedure_name = node.children[0].val
                    matching_method_symbol = None
                    for symbol in self.symbolTable.symbols:
                        if symbol.name == procedure_name and symbol.id_type == "Method":
                            matching_method_symbol = symbol
                            break
                    if matching_method_symbol:
                        self.symbolTable.insert(Symbol(procedure_name, "MethodCall", "Void", self.getExprChildren(node.children[2]), None, class_scope + "." + method_scope, node.line))
                    else:
                        
                        self.symbolTable.insert(Symbol(procedure_name, "Procedure", "Void", self.getExprChildren(node.children[2]), None, class_scope + "." + method_scope, node.line))

                elif rule_name == "expr" and len(node.children) > 4 and node.children[1].val == "(" and node.children[-1].val == ")":
                    methodName = node.children[0].val
                    children = node.children[2:-1]
                    childrenStrings = []
                    for child in children:
                        if child.val == "expr":
                            childrenStrings.append(self.getExprChildren(child))
                        else:
                            childrenStrings.append(child.val)
                    
                    childrenStr = "".join(childrenStrings)
                    self.symbolTable.insert(Symbol(methodName, "MethodCall", "Void", childrenStr, None, class_scope + "." + method_scope, node.line))

        claseActual = ""
        for symbol in self.symbolTable.symbols:
            if symbol.inheritsFrom:
                claseActual = symbol.inheritsFrom
                claseHeredando = symbol.name
                for symbol2 in self.symbolTable.symbols:
                    if claseHeredando in symbol2.scope and symbol2.name != "constructor":
                        try:
                            if symbol2.name in classProperties[claseActual]:
                                symbol2.inheritsFrom = claseActual
                        except:
                            pass
        
            if symbol.value is None and symbol.id_type == "Variable":
                if symbol.data_type == "String":
                    symbol.update_value("")
                elif symbol.data_type == "Int":
                    symbol.update_value(0)
                elif symbol.data_type == "Bool":
                    symbol.update_value('false')
                
        print("\n --Simbolos --")
        
        # Asignar los bytes a cada variable de tipo Int, String y Bool:
        for symbol in self.symbolTable.symbols:
            if symbol.data_type == "Int" and symbol.id_type == "Variable":
                symbol.bytes = 4
            elif symbol.data_type == "String" and symbol.id_type == "Variable":
                print(symbol)
                symbol.bytes = len(symbol.value) + 1
            elif symbol.data_type == "Bool" and symbol.id_type == "Variable":
                symbol.bytes = 1

        # Mapear cada variable/funcion con su direccion de memoria:
        memory_address = 0
        for symbol in self.symbolTable.symbols:
            if symbol.id_type == "Variable":
                symbol.memory_address = memory_address
                memory_address += symbol.bytes
            elif symbol.id_type == "Method":
                symbol.memory_address = memory_address
                memory_address += 1
            elif symbol.id_type == "MethodCall":
                symbol.memory_address = memory_address
                memory_address += 1
            elif symbol.id_type == "Procedure":
                symbol.memory_address = memory_address
                memory_address += 1
            elif symbol.id_type == "Class":
                symbol.memory_address = memory_address
                memory_address += 1
            elif symbol.id_type == "Parameter":
                symbol.memory_address = memory_address
                memory_address += symbol.bytes

        self.symbolTable.display()

    def semanticAnalysis(self):
        print("\n------SEMANTIC ANALYZER------")
        self.semanticAnalyzer = SemanticAnalyzer(self.treeStruct, self.symbolTable, self.tokens)
        self.semanticAnalyzer.analyze()
        print("\n-----------------------------")

    
    def getExprChildren(self, node, child_values=None):
        if child_values is None:
            child_values = []  # Initialize the list only in the initial call
        
        for child in node.children:
            if child.val == "expr":
                self.getExprChildren(child, child_values)  # Pass the existing list to the recursive call
            else:
                child_values.append(child.val)
        
        return ' '.join(child_values)


    def extract_method_return_type(self, method_node):
        colon_found = False
        method_type = ""

        for child in method_node.children:
            if colon_found:
                if child.val == "{":
                    break
                method_type += child.val
            elif child.val == ":":
                colon_found = True

        return method_type.strip()

    def syntacticAnalysis2(self):
        if self.error_listener.errors:
            print("\nERRORES SINTÁCTICOS IDENTIFICADOS:")
            for error in self.error_listener.errors:
                print(error)
        else:
            print("\nARBOL SINTÁCTICO GENERADO:")
            command = f"antlr4-parse Proyecto3/YAPL.g4 program  -gui {self.input}"
            os.system(command)



    def build_tree(self, node, parent=None):
        if node is not None:
            # Get the rule name for rule context objects
            if isinstance(node, RuleContext):
                rule_index = node.getRuleIndex()
                rule_name = self.parser.ruleNames[rule_index]
                # print("RuleName:",rule_name)
                tree_node = AbstractTreeNode(rule_name)
            else:
                tree_node = AbstractTreeNode(str(node))
            
            # Set the errorNode Variable to True if the node represents an error
            if isinstance(node, ErrorNode):
                tree_node.errorNode = True

            if parent is not None:
                tree_node.parent = parent
            
            if isinstance(node, ParserRuleContext):
                tree_node.line = node.start.line

            # Recursively build the tree for each child node
            if not isinstance(node, TerminalNodeImpl):
                for child in node.children:
                    child_tree_node = self.build_tree(child, tree_node)
                    tree_node.add_child(child_tree_node)
            
            return tree_node

    def traverse_tree(self, node, tree):
        if node is not None:
            tree.add_node(node)
            for child in node.children:
                self.traverse_tree(child, tree)

    def get_tokens(self):
        self.token_stream.fill()
        all_tokens = self.token_stream.tokens
        good_tokens = []

        token_type_names = {1: "';'", 2: "'{'", 3: "'}'", 4: "'('", 5: "','", 6: "')'", 7: "':'", 8: "'@'", 9: "'.'", 10: "'~'", 11: "'*'", 12: "'/'", 13: "'+'", 14: "'-'", 15: "'<='", 16: "'<'", 17: "'='", 18: "WHITESPACE", 19: "BLOCK_COMMENT", 20: "LINE_COMMENT", 21: "CLASS", 22: "ELSE", 23: "FALSE", 24: "FI", 25: "IF", 26: "IN", 27: "INHERITS", 28: "ISVOID", 29: "LET", 30: "LOOP", 31: "POOL", 32: "THEN", 33: "WHILE", 34: "CASE", 35: "ESAC", 36: "NEW", 37: "OF", 38: "NOT", 39: "TRUE", 40: "STRING", 41: "INT", 42: "TYPE", 43: "ID", 44: "'<-'", 45: "'=>'", 46: "ERROR"}

        line = column = 1 
        last_line = 1

        # Iterate through all tokens
        for token in all_tokens:
            # Skip the EOF token
            if token.type == Token.EOF:
                continue

            token_type = token.type
            token_name = token_type_names.get(token_type, f"Unknown token ({token_type})")
            lexeme = token.text
            self.tokens[lexeme] = token_name

            # Calculate line and column information
            if last_line != token.line:
                line += 1
                column = 1
                last_line = token.line
            else:
                column += len(lexeme)

            if token_name == "ERROR":
                self.lexicalErrors.append(f"{token_name} Lexical: Character '{lexeme}' not found")
            else:
                good_tokens.append(f"Token Type: {token_name}, " f"Value: {lexeme}")

        return good_tokens, self.lexicalErrors
    

class AbstractTreeNode():
    def __init__(self, val):
        self.val = val
        self.errorNode = False
        self.children = []
        self.parent = None
        self.line = None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def __str__(self):
        s = f"TreeNode: {self.val}"
        s += f"\n\tErrorNode: {self.errorNode}"
        if len(self.children) > 0:
            s += f"\n\tChildren: {[child.val for child in self.children]}"
        if self.parent:
            s += f"\n\tParent: {self.parent.val}"
        s += f"\n\tLine: {self.line}"
        return s
    
class AbstractTree():
    def __init__(self):
        self.root = None
        self.nodes = []
    
    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        s = f"AbstractTree: {self.root.val}"
        if len(self.nodes) > 0:
            s += f"\n\tNodes: {[node.val for node in self.nodes]}"
        return s