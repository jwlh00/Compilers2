from prettytable.prettytable import NONE
from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from antlr4.error.ErrorListener import ErrorListener
from YAPLLexer import YAPLLexer
from YAPLListener import YAPLListener
from YAPLParser import YAPLParser
from itertools import groupby
from YAPL_Printer import YAPLPrinter
from TranslateToTAC import TACTranslator
from TranslatetoMIPS import *

class errorListener(ErrorListener):
    def __init__(self):
        self.hasError = False
        self.listErrors = []
        pass

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hasError = True
        errorMsg = f'=> Se encontro un error en {line}:{column}. El caracter causante es: {offendingSymbol.text}'
        self.listErrors.append(errorMsg)
    
    def getHasError(self):
        return self.hasError

class Compile():
    def __init__(self, url):
        self.printer = None
        input = FileStream(url)
        self.lexer = YAPLLexer(input)
        self.lexer.removeErrorListeners()
        stream = CommonTokenStream(self.lexer)
        parser = YAPLParser(stream)
        self.myError = errorListener() 
        parser.removeErrorListeners()
        parser.addErrorListener(self.myError)
        tree = parser.program()
        self.tac_code = []
        self.tac_quadruples = []

        print("\nTokens encontrados: ")
        self.print_tokens()

        if self.myError.getHasError():

            self.printer = YAPLPrinter()
            walker = ParseTreeWalker()
            walker.walk(self.printer, tree)
            print("\nReporte de errores: Lexicos y Sintacticos")
            for i in self.myError.listErrors:
                print(i)
        else:
            self.printer = YAPLPrinter()
            walker = ParseTreeWalker()
            walker.walk(self.printer, tree)
            # print("\nArbol de parseo en string: ")
            # print(tree.toStringTree(recog=parser))

            self.tac_translator = TACTranslator()
            self.tac_translator.translate(tree)


            # Print the quadruples
            self.tac_quadruples = self.tac_translator.get_quadruples()
            print(self.tac_quadruples)
            for quad in self.tac_quadruples:
                print(quad)
            print("===========================")
            self.tac_code = self.tac_translator.get_TAC()
            print("TAC Code:")
            print("===========================")
            print(self.tac_code)
            print("===========================")
            # print(self.tac_translator.get_TACDebug())
            print("MIP Code:")
            print(generate_mips_from_tac_final(self.tac_quadruples))

    def get_tac_code(self):
        return self.tac_code

    def print_tokens(self):
        # Tokenize the input
        self.lexer.reset()
        token = self.lexer.nextToken()
        # Iterate over all the tokens
        while token.type != Token.EOF:
            print(f"Tipo de token: {self.getType(token.type)}, Valor: {token.text}")
            token = self.lexer.nextToken()
    
    def getType(self, tokenType):
        # Match the YAPLLexer.tokens to the tokenType with ifs
        if tokenType == self.lexer.ID:
            return "ID"
        elif tokenType == self.lexer.STR_CONST:
            return "STR_CONST"
        elif tokenType == self.lexer.INT_CONST:
            return "INT_CONST"
        elif tokenType == self.lexer.WS:
            return "WS"
        elif tokenType == self.lexer.BOOL:
            return "BOOL"
        elif tokenType == self.lexer.STRING:
            return "STRING"
        elif tokenType == self.lexer.INT:
            return "INT"
        elif tokenType == self.lexer.IO:
            return "IO"
        elif tokenType == self.lexer.SELF_TYPE:
            return "SELF_TYPE"
        elif tokenType == self.lexer.CASE:
            return "CASE"
        elif tokenType == self.lexer.OF:
            return "OF"
        elif tokenType == self.lexer.ESAC:
            return "ESAC"
        elif tokenType == self.lexer.NEW:
            return "NEW"
        elif tokenType == self.lexer.ISVOID:
            return "ISVOID"
        elif tokenType == self.lexer.NOT:
            return "NOT"
        elif tokenType == self.lexer.ASSIGN:
            return "ASSIGN"
        elif tokenType == self.lexer.ARROW:
            return "ARROW"
        elif tokenType == self.lexer.SEMI:
            return "SEMI"
        elif tokenType == self.lexer.COLON:
            return "COLON"
        elif tokenType == self.lexer.COMMA:
            return "COMMA"
        elif tokenType == self.lexer.DOT:
            return "DOT"
        elif tokenType == self.lexer.LPAREN:
            return "LPAREN"
        elif tokenType == self.lexer.RPAREN:
            return "RPAREN"
        elif tokenType == self.lexer.LBRACE:
            return "LBRACE"
        elif tokenType == self.lexer.RBRACE:
            return "RBRACE"
        elif tokenType == self.lexer.LINE_COMMENT:
            return "LINE_COMMENT"
        elif tokenType == self.lexer.COMMENT:
            return "COMMENT"
        elif self.lexer.T__0 <= tokenType <= self.lexer.T__26:
            return "KEYWORD"
        else:
            return "ERROR"

compile = Compile("./test.yapl")
# compile = Compile("./test_medio.yapl")