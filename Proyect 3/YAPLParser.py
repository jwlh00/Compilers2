# Generated from YAPL.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
from antlr4.error.ErrorListener import ErrorListener
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,204,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,1,
        1,1,1,2,1,2,3,2,45,8,2,1,3,1,3,1,3,1,3,1,3,5,3,52,8,3,10,3,12,3,
        55,9,3,5,3,57,8,3,10,3,12,3,60,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,3,4,72,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,5,7,88,8,7,10,7,12,7,91,9,7,5,7,93,8,7,10,7,12,7,96,
        9,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,4,7,117,8,7,11,7,12,7,118,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,4,7,131,8,7,11,7,12,7,132,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,5,7,158,8,7,10,7,12,7,161,9,7,1,7,1,7,1,7,3,7,166,8,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,180,8,7,1,7,1,
        7,1,7,1,7,1,7,1,7,5,7,188,8,7,10,7,12,7,191,9,7,5,7,193,8,7,10,7,
        12,7,196,9,7,1,7,5,7,199,8,7,10,7,12,7,202,9,7,1,7,0,1,14,8,0,2,
        4,6,8,10,12,14,0,4,2,0,23,23,39,39,1,0,11,12,1,0,13,14,1,0,15,17,
        229,0,19,1,0,0,0,2,25,1,0,0,0,4,44,1,0,0,0,6,46,1,0,0,0,8,68,1,0,
        0,0,10,73,1,0,0,0,12,77,1,0,0,0,14,165,1,0,0,0,16,17,3,2,1,0,17,
        18,5,1,0,0,18,20,1,0,0,0,19,16,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,
        0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,5,
        21,0,0,26,29,5,42,0,0,27,28,5,27,0,0,28,30,5,42,0,0,29,27,1,0,0,
        0,29,30,1,0,0,0,30,31,1,0,0,0,31,37,5,2,0,0,32,33,3,4,2,0,33,34,
        5,1,0,0,34,36,1,0,0,0,35,32,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,
        37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,3,0,0,41,3,1,0,
        0,0,42,45,3,6,3,0,43,45,3,8,4,0,44,42,1,0,0,0,44,43,1,0,0,0,45,5,
        1,0,0,0,46,47,5,43,0,0,47,58,5,4,0,0,48,53,3,12,6,0,49,50,5,5,0,
        0,50,52,3,12,6,0,51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,
        1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,56,48,1,0,0,0,57,60,1,0,0,0,
        58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,62,5,
        6,0,0,62,63,5,7,0,0,63,64,5,42,0,0,64,65,5,2,0,0,65,66,3,14,7,0,
        66,67,5,3,0,0,67,7,1,0,0,0,68,71,3,12,6,0,69,70,5,44,0,0,70,72,3,
        14,7,0,71,69,1,0,0,0,71,72,1,0,0,0,72,9,1,0,0,0,73,74,5,43,0,0,74,
        75,5,44,0,0,75,76,3,14,7,0,76,11,1,0,0,0,77,78,5,43,0,0,78,79,5,
        7,0,0,79,80,5,42,0,0,80,13,1,0,0,0,81,82,6,7,-1,0,82,83,5,43,0,0,
        83,94,5,4,0,0,84,89,3,14,7,0,85,86,5,5,0,0,86,88,3,14,7,0,87,85,
        1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,93,1,0,0,0,
        91,89,1,0,0,0,92,84,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,
        0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,166,5,6,0,0,98,99,5,25,0,0,
        99,100,3,14,7,0,100,101,5,32,0,0,101,102,3,14,7,0,102,103,5,22,0,
        0,103,104,3,14,7,0,104,105,5,24,0,0,105,166,1,0,0,0,106,107,5,33,
        0,0,107,108,3,14,7,0,108,109,5,30,0,0,109,110,3,14,7,0,110,111,5,
        31,0,0,111,166,1,0,0,0,112,116,5,2,0,0,113,114,3,14,7,0,114,115,
        5,1,0,0,115,117,1,0,0,0,116,113,1,0,0,0,117,118,1,0,0,0,118,116,
        1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,121,5,3,0,0,121,166,
        1,0,0,0,122,123,5,34,0,0,123,124,3,14,7,0,124,130,5,37,0,0,125,126,
        3,12,6,0,126,127,5,45,0,0,127,128,3,14,7,0,128,129,5,1,0,0,129,131,
        1,0,0,0,130,125,1,0,0,0,131,132,1,0,0,0,132,130,1,0,0,0,132,133,
        1,0,0,0,133,134,1,0,0,0,134,135,5,35,0,0,135,166,1,0,0,0,136,137,
        5,36,0,0,137,166,5,42,0,0,138,139,5,10,0,0,139,166,3,14,7,13,140,
        141,5,28,0,0,141,166,3,14,7,12,142,143,5,38,0,0,143,166,3,14,7,8,
        144,145,5,4,0,0,145,146,3,14,7,0,146,147,5,6,0,0,147,166,1,0,0,0,
        148,166,5,43,0,0,149,166,5,41,0,0,150,166,5,40,0,0,151,166,7,0,0,
        0,152,166,3,10,5,0,153,154,5,29,0,0,154,159,3,8,4,0,155,156,5,5,
        0,0,156,158,3,8,4,0,157,155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,
        0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,163,5,26,
        0,0,163,164,3,14,7,1,164,166,1,0,0,0,165,81,1,0,0,0,165,98,1,0,0,
        0,165,106,1,0,0,0,165,112,1,0,0,0,165,122,1,0,0,0,165,136,1,0,0,
        0,165,138,1,0,0,0,165,140,1,0,0,0,165,142,1,0,0,0,165,144,1,0,0,
        0,165,148,1,0,0,0,165,149,1,0,0,0,165,150,1,0,0,0,165,151,1,0,0,
        0,165,152,1,0,0,0,165,153,1,0,0,0,166,200,1,0,0,0,167,168,10,11,
        0,0,168,169,7,1,0,0,169,199,3,14,7,12,170,171,10,10,0,0,171,172,
        7,2,0,0,172,199,3,14,7,11,173,174,10,9,0,0,174,175,7,3,0,0,175,199,
        3,14,7,10,176,179,10,20,0,0,177,178,5,8,0,0,178,180,5,42,0,0,179,
        177,1,0,0,0,179,180,1,0,0,0,180,181,1,0,0,0,181,182,5,9,0,0,182,
        183,5,43,0,0,183,194,5,4,0,0,184,189,3,14,7,0,185,186,5,5,0,0,186,
        188,3,14,7,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,
        190,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,192,184,1,0,0,0,193,
        196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,197,1,0,0,0,196,
        194,1,0,0,0,197,199,5,6,0,0,198,167,1,0,0,0,198,170,1,0,0,0,198,
        173,1,0,0,0,198,176,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,
        201,1,0,0,0,201,15,1,0,0,0,202,200,1,0,0,0,18,21,29,37,44,53,58,
        71,89,94,118,132,159,165,179,189,194,198,200
    ]

class YAPLParser ( Parser ):

    grammarFileName = "YAPL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'('", "','", "')'", 
                     "':'", "'@'", "'.'", "'~'", "'*'", "'/'", "'+'", "'-'", 
                     "'<='", "'<'", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'true'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<-'", "'=>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WHITESPACE", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "CLASS", "ELSE", "FALSE", "FI", "IF", 
                      "IN", "INHERITS", "ISVOID", "LET", "LOOP", "POOL", 
                      "THEN", "WHILE", "CASE", "ESAC", "NEW", "OF", "NOT", 
                      "TRUE", "STRING", "INT", "TYPE", "ID", "ASSIGNMENT", 
                      "IMPLY", "ERROR" ]

    RULE_program = 0
    RULE_classDefine = 1
    RULE_feature_list = 2
    RULE_method = 3
    RULE_property = 4
    RULE_varDeclaration = 5
    RULE_formal = 6
    RULE_expr = 7

    ruleNames =  [ "program", "classDefine", "feature_list", "method", "property", 
                   "varDeclaration", "formal", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    WHITESPACE=18
    BLOCK_COMMENT=19
    LINE_COMMENT=20
    CLASS=21
    ELSE=22
    FALSE=23
    FI=24
    IF=25
    IN=26
    INHERITS=27
    ISVOID=28
    LET=29
    LOOP=30
    POOL=31
    THEN=32
    WHILE=33
    CASE=34
    ESAC=35
    NEW=36
    OF=37
    NOT=38
    TRUE=39
    STRING=40
    INT=41
    TYPE=42
    ID=43
    ASSIGNMENT=44
    IMPLY=45
    ERROR=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(YAPLParser.EOF, 0)

        def classDefine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ClassDefineContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ClassDefineContext,i)


        def getRuleIndex(self):
            return YAPLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = YAPLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.classDefine()
                self.state = 17
                self.match(YAPLParser.T__0)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 23
            self.match(YAPLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(YAPLParser.CLASS, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLParser.TYPE)
            else:
                return self.getToken(YAPLParser.TYPE, i)

        def INHERITS(self):
            return self.getToken(YAPLParser.INHERITS, 0)

        def feature_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.Feature_listContext)
            else:
                return self.getTypedRuleContext(YAPLParser.Feature_listContext,i)


        def getRuleIndex(self):
            return YAPLParser.RULE_classDefine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDefine" ):
                listener.enterClassDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDefine" ):
                listener.exitClassDefine(self)




    def classDefine(self):

        localctx = YAPLParser.ClassDefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDefine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(YAPLParser.CLASS)
            self.state = 26
            self.match(YAPLParser.TYPE)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 27
                self.match(YAPLParser.INHERITS)
                self.state = 28
                self.match(YAPLParser.TYPE)


            self.state = 31
            self.match(YAPLParser.T__1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 32
                self.feature_list()
                self.state = 33
                self.match(YAPLParser.T__0)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(YAPLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Feature_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(YAPLParser.MethodContext,0)


        def property_(self):
            return self.getTypedRuleContext(YAPLParser.PropertyContext,0)


        def getRuleIndex(self):
            return YAPLParser.RULE_feature_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature_list" ):
                listener.enterFeature_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature_list" ):
                listener.exitFeature_list(self)




    def feature_list(self):

        localctx = YAPLParser.Feature_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feature_list)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.property_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)

        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.FormalContext)
            else:
                return self.getTypedRuleContext(YAPLParser.FormalContext,i)


        def getRuleIndex(self):
            return YAPLParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)




    def method(self):

        localctx = YAPLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(YAPLParser.ID)
            self.state = 47
            self.match(YAPLParser.T__3)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 48
                self.formal()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 49
                    self.match(YAPLParser.T__4)
                    self.state = 50
                    self.formal()
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(YAPLParser.T__5)
            self.state = 62
            self.match(YAPLParser.T__6)
            self.state = 63
            self.match(YAPLParser.TYPE)
            self.state = 64
            self.match(YAPLParser.T__1)
            self.state = 65
            self.expr(0)
            self.state = 66
            self.match(YAPLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formal(self):
            return self.getTypedRuleContext(YAPLParser.FormalContext,0)


        def ASSIGNMENT(self):
            return self.getToken(YAPLParser.ASSIGNMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def getRuleIndex(self):
            return YAPLParser.RULE_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProperty" ):
                listener.enterProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProperty" ):
                listener.exitProperty(self)




    def property_(self):

        localctx = YAPLParser.PropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_property)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.formal()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 69
                self.match(YAPLParser.ASSIGNMENT)
                self.state = 70
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def ASSIGNMENT(self):
            return self.getToken(YAPLParser.ASSIGNMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def getRuleIndex(self):
            return YAPLParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)




    def varDeclaration(self):

        localctx = YAPLParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(YAPLParser.ID)
            self.state = 74
            self.match(YAPLParser.ASSIGNMENT)
            self.state = 75
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)

        def getRuleIndex(self):
            return YAPLParser.RULE_formal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal" ):
                listener.enterFormal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal" ):
                listener.exitFormal(self)




    def formal(self):

        localctx = YAPLParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_formal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(YAPLParser.ID)
            self.state = 78
            self.match(YAPLParser.T__6)
            self.state = 79
            self.match(YAPLParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return YAPLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NewContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(YAPLParser.NEW, 0)
        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNew" ):
                listener.enterNew(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNew" ):
                listener.exitNew(self)


    class ParenthesesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)


    class LetInContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(YAPLParser.LET, 0)
        def property_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.PropertyContext)
            else:
                return self.getTypedRuleContext(YAPLParser.PropertyContext,i)

        def IN(self):
            return self.getToken(YAPLParser.IN, 0)
        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetIn" ):
                listener.enterLetIn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetIn" ):
                listener.exitLetIn(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(YAPLParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class IsvoidContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISVOID(self):
            return self.getToken(YAPLParser.ISVOID, 0)
        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsvoid" ):
                listener.enterIsvoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsvoid" ):
                listener.exitIsvoid(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varDeclaration(self):
            return self.getTypedRuleContext(YAPLParser.VarDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)


    class ArithmeticContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)


    class WhileContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(YAPLParser.WHILE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def LOOP(self):
            return self.getToken(YAPLParser.LOOP, 0)
        def POOL(self):
            return self.getToken(YAPLParser.POOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)


    class DispatchImplicitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDispatchImplicit" ):
                listener.enterDispatchImplicit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDispatchImplicit" ):
                listener.exitDispatchImplicit(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(YAPLParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)


    class NegativeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative" ):
                listener.enterNegative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative" ):
                listener.exitNegative(self)


    class BoolNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(YAPLParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(YAPLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolNot" ):
                listener.enterBoolNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolNot" ):
                listener.exitBoolNot(self)


    class BooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(YAPLParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(YAPLParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)


    class BlockContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)


    class ComparissonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisson" ):
                listener.enterComparisson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisson" ):
                listener.exitComparisson(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(YAPLParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def THEN(self):
            return self.getToken(YAPLParser.THEN, 0)
        def ELSE(self):
            return self.getToken(YAPLParser.ELSE, 0)
        def FI(self):
            return self.getToken(YAPLParser.FI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)


    class CaseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(YAPLParser.CASE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def OF(self):
            return self.getToken(YAPLParser.OF, 0)
        def ESAC(self):
            return self.getToken(YAPLParser.ESAC, 0)
        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.FormalContext)
            else:
                return self.getTypedRuleContext(YAPLParser.FormalContext,i)

        def IMPLY(self, i:int=None):
            if i is None:
                return self.getTokens(YAPLParser.IMPLY)
            else:
                return self.getToken(YAPLParser.IMPLY, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase" ):
                listener.enterCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase" ):
                listener.exitCase(self)


    class DispatchExplicitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YAPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YAPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(YAPLParser.ExprContext,i)

        def ID(self):
            return self.getToken(YAPLParser.ID, 0)
        def TYPE(self):
            return self.getToken(YAPLParser.TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDispatchExplicit" ):
                listener.enterDispatchExplicit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDispatchExplicit" ):
                listener.exitDispatchExplicit(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = YAPLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = YAPLParser.DispatchImplicitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 82
                self.match(YAPLParser.ID)
                self.state = 83
                self.match(YAPLParser.T__3)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13014598157332) != 0):
                    self.state = 84
                    self.expr(0)
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 85
                        self.match(YAPLParser.T__4)
                        self.state = 86
                        self.expr(0)
                        self.state = 91
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 97
                self.match(YAPLParser.T__5)
                pass

            elif la_ == 2:
                localctx = YAPLParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(YAPLParser.IF)
                self.state = 99
                self.expr(0)
                self.state = 100
                self.match(YAPLParser.THEN)
                self.state = 101
                self.expr(0)
                self.state = 102
                self.match(YAPLParser.ELSE)
                self.state = 103
                self.expr(0)
                self.state = 104
                self.match(YAPLParser.FI)
                pass

            elif la_ == 3:
                localctx = YAPLParser.WhileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(YAPLParser.WHILE)
                self.state = 107
                self.expr(0)
                self.state = 108
                self.match(YAPLParser.LOOP)
                self.state = 109
                self.expr(0)
                self.state = 110
                self.match(YAPLParser.POOL)
                pass

            elif la_ == 4:
                localctx = YAPLParser.BlockContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(YAPLParser.T__1)
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 113
                    self.expr(0)
                    self.state = 114
                    self.match(YAPLParser.T__0)
                    self.state = 118 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 13014598157332) != 0)):
                        break

                self.state = 120
                self.match(YAPLParser.T__2)
                pass

            elif la_ == 5:
                localctx = YAPLParser.CaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(YAPLParser.CASE)
                self.state = 123
                self.expr(0)
                self.state = 124
                self.match(YAPLParser.OF)
                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 125
                    self.formal()
                    self.state = 126
                    self.match(YAPLParser.IMPLY)
                    self.state = 127
                    self.expr(0)
                    self.state = 128
                    self.match(YAPLParser.T__0)
                    self.state = 132 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==43):
                        break

                self.state = 134
                self.match(YAPLParser.ESAC)
                pass

            elif la_ == 6:
                localctx = YAPLParser.NewContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.match(YAPLParser.NEW)
                self.state = 137
                self.match(YAPLParser.TYPE)
                pass

            elif la_ == 7:
                localctx = YAPLParser.NegativeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(YAPLParser.T__9)
                self.state = 139
                self.expr(13)
                pass

            elif la_ == 8:
                localctx = YAPLParser.IsvoidContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(YAPLParser.ISVOID)
                self.state = 141
                self.expr(12)
                pass

            elif la_ == 9:
                localctx = YAPLParser.BoolNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(YAPLParser.NOT)
                self.state = 143
                self.expr(8)
                pass

            elif la_ == 10:
                localctx = YAPLParser.ParenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(YAPLParser.T__3)
                self.state = 145
                self.expr(0)
                self.state = 146
                self.match(YAPLParser.T__5)
                pass

            elif la_ == 11:
                localctx = YAPLParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(YAPLParser.ID)
                pass

            elif la_ == 12:
                localctx = YAPLParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(YAPLParser.INT)
                pass

            elif la_ == 13:
                localctx = YAPLParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(YAPLParser.STRING)
                pass

            elif la_ == 14:
                localctx = YAPLParser.BooleanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                localctx.value = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==23 or _la==39):
                    localctx.value = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 15:
                localctx = YAPLParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.varDeclaration()
                pass

            elif la_ == 16:
                localctx = YAPLParser.LetInContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(YAPLParser.LET)
                self.state = 154
                self.property_()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 155
                    self.match(YAPLParser.T__4)
                    self.state = 156
                    self.property_()
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 162
                self.match(YAPLParser.IN)
                self.state = 163
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 198
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = YAPLParser.ArithmeticContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 168
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = YAPLParser.ArithmeticContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 171
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 172
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = YAPLParser.ComparissonContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 174
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 175
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = YAPLParser.DispatchExplicitContext(self, YAPLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 179
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==8:
                            self.state = 177
                            self.match(YAPLParser.T__7)
                            self.state = 178
                            self.match(YAPLParser.TYPE)


                        self.state = 181
                        self.match(YAPLParser.T__8)
                        self.state = 182
                        self.match(YAPLParser.ID)
                        self.state = 183
                        self.match(YAPLParser.T__3)
                        self.state = 194
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13014598157332) != 0):
                            self.state = 184
                            self.expr(0)
                            self.state = 189
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==5:
                                self.state = 185
                                self.match(YAPLParser.T__4)
                                self.state = 186
                                self.expr(0)
                                self.state = 191
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)

                            self.state = 196
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 197
                        self.match(YAPLParser.T__5)
                        pass

             
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 20)
         

class SemanticVisitor:
    def __init__(self, symbol_table, tokenDict):
        self.symbol_table = symbol_table
        self.tokenDict = tokenDict
        self.names, self.ids, self.dataTypes, self.values, self.inheritsFroms, self.scopes, self.lines = self.symbol_table.allInfo()

    # Verificar que exista clase main
    def visit_program_node(self, node):
        MainClass = False
        for children in node.children:
            if children.val == "classDefine":
                if children.children[1].val == "Main":
                    MainClass = True
        
        if not MainClass:
            return f"El programa debe tener una clase 'Main'"
        return None

    # Verificar si alguna clase hereda a main o viceversa
    def visit_classdefine_node(self, node):
        class_name = node.children[1].val
        method_names = [symbol.name for symbol in self.symbol_table.symbols if symbol.id_type == "Method" and symbol.scope.startswith(class_name)]
        
        #ver si hace falta la clase main
        if class_name == "Main" and "main" not in method_names:
            return f"La clase 'Main' debe tener un metodo 'main'"
        #ver si alguna clase hereda a Main
        if node.children[2].val == "inherits" and node.children[3].val == "Main":
            return f"La clase 'Main' no puede ser heredar por ninguna otra clase"
        
        elif node.children[2].val == "inherits" and node.children[3].val == "String":
            return f"La clase 'String' no puede ser heredar por ninguna otra clase"
        
        elif node.children[2].val == "inherits" and node.children[3].val == "Int":
            return f"La clase 'Int' no puede ser heredar por ninguna otra clase"
        
        elif node.children[2].val == "inherits" and node.children[3].val == "Bool":
            return f"La clase 'Bool' no puede ser heredar por ninguna otra clase"
        
        if node.children[2].val == "inherits" and class_name == "Main":
            return f"La clase 'Main' no puede heredar de ninguna otra clase"

        if node.children[2].val == "inherits" and node.children[3].val == class_name:
            return f"La clase '{class_name}' no puede heredar de si misma (herencia recursiva)"
        
        return None


    # Verifica que los metodos heredados sigan la firma del origina y que exista el metodo main
    def visit_method_node(self, node):
        methodName = node.children[0].val
        nodeScope = node.parent.parent.children[1].val
        
        if methodName == "main" and node.children[2].val == "formal":
            return f"El metodo 'main' no puede tener parametros formales"
        
        #ver que los metodos heredadeos sigan la firma del original
        symbolToUse = self.symbol_table.lookup_by_scope(methodName, nodeScope)
        # print(symbolToUse)
        if symbolToUse.inheritsFrom:
            # print(symbolToUse)
            inheritedFrom = symbolToUse.inheritsFrom
            symbolToMatch = self.symbol_table.lookup_by_scope(methodName, inheritedFrom)
            # print(symbolToMatch)
            if symbolToMatch.data_type != symbolToUse.data_type:
                return f"El metodo '{methodName}' en el scope '{nodeScope}' debe tener el mismo tipo de retorno que el metodo original en el scope '{inheritedFrom}'"


    def visit_vardeclaration_node(self, node):
        #revisar si la variable ya fue definida
        var_name = node.children[0].val
        for symbol in self.symbol_table.symbols:
            if symbol.name == var_name and symbol.id_type == "Variable" and symbol.data_type == "Void":
                return f"La variable '{var_name}' no ha sido definida"

        #revisar que las asignaciones esten en el mismo scope
        varScope = self.symbol_table.lookup_all(var_name).scope
        children = self.getExprChildren(node.children[2])
        for child in children:
            if child in self.names:
                childScope = self.symbol_table.lookup_all(child).scope
                if childScope.split(".")[0] != varScope.split(".")[0]:
                    return f"El atributo '{child}' no ha sido definida en el scope '{varScope}'"
        #revisar que los tipos sean los correctos

        #obtener el tipo de la variable
        var_type = None
        for symbol in self.symbol_table.symbols:
            if symbol.name == var_name:
                var_type = symbol.data_type

        # print("var_name: ", var_name, "var_type: ", var_type)
        #revisar por asignaciones correctas
        expr_node = node.children[2]

        if len(expr_node.children) == 1:
            value_node = expr_node.children[0]
            
            # Verifica que las variables se aignen con el mismo tipo
            if value_node.val in self.names:
                symbol = self.symbol_table.lookup(value_node.val)
                if symbol.data_type != var_type:
                    if var_type.lower() == "int" and symbol.data_type.lower() == "bool":
                        if symbol.value:
                            self.symbol_table.update_symbol_value(var_name, 1)
                        else:
                            self.symbol_table.update_symbol_value(var_name, 0)
                        self.symbol_table.display()
                    elif var_type.lower() == "bool" and symbol.data_type.lower() == "int":
                        if symbol.value == "0":

                            self.symbol_table.update_symbol_value(var_name, False)
                        else:

                            self.symbol_table.update_symbol_value(var_name, True)
                        self.symbol_table.display()
                    else:
                        return f"La variable '{var_name}' debe ser de tipo '{var_type}' no '{symbol.data_type}'"
            
            # Verifica que los tokens se asignen con el mismo tipo
            elif value_node.val in self.tokenDict:
                valueType = self.tokenDict[value_node.val]
                
                if valueType.lower() != var_type.lower():
                    if var_type.lower() == "int" and valueType.lower() == "bool":
                        print(var_name)
                    elif var_type.lower() == "bool" and valueType.lower() == "int":
                        pass
                    else:
                        if symbol.data_type.lower() == "id" or symbol.data_type.lower() == "void": #este no
                            return f"El atributo '{value_node.val}' no ha sido definido en el scope '{varScope}'"
                        else:
                            return f"La variable '{var_name}' debe ser de tipo '{var_type}' no '{symbol.data_type}'"

        
        else:
            child_values = self.getExprChildren(expr_node)
            operators = []
            alphanum = []
            variables = {}

            stringOperators = ["+", ","]
            intOperators = ["+", "-", "*", "/", "%", "(", ")","~"]

           
            #Verifica que hayan operadores dentro de la asignacion x <- 1 + 2
            for child in child_values:
                if child.isalnum():
                    # print(child)
                    if child in self.names:
                        symbol = self.symbol_table.lookup(child)
                        variables[child] = symbol.data_type
                        alphanum.append(child)
                    else:
                        variables[child] = self.tokenDict[child]  
                        alphanum.append(child)
                elif '"' in child:
                    variables[child] = "String"
                    alphanum.append(child)
                else:
                    operators.append(child)

            # print("alphanum: ", alphanum)
            # print("variables: ", variables)
            # Verifica y asigna el return de un metodo
            if "(" in operators and ")" in operators and operators.count("(") == 1 and operators.count(")") == 1:
                symbol_type = self.symbol_table.lookup_by_scope(alphanum[0], varScope)
                symbol_type_2 = symbol_type.data_type
                if symbol_type_2.lower() != var_type.lower():
                    return f"La variable '{alphanum[0]}' debe ser de tipo '{var_type}' no '{symbol_type_2}'"
                return None

            # print(operators)

            # Verifica que las variables se aignen con el mismo tipo
            firstVal = next(iter(variables.values())).lower()
            if all(value.lower() == firstVal for value in variables.values()):
                if firstVal.lower() != var_type.lower():
                    return f"Las variables '{alphanum}' deben ser de tipo '{var_type}' no '{firstVal}'"

                elif firstVal.lower() == var_type.lower() and firstVal.lower() == "string":
                    for operator in operators:
                        if operator not in stringOperators:
                            return f"La operacion '{operator}' no es valida para variables de tipo '{firstVal}'"
              
                elif firstVal.lower() == var_type.lower() and firstVal.lower() == "int":
                    for operator in operators:
                        if operator not in intOperators:
                            return f"La operacion '{operator}' no es valida para variables de tipo '{firstVal}'"
            else:
                for var in alphanum:
                    if var not in self.names and self.tokenDict[var].lower() == "id":
                        return f"El atributo '{var}' no ha sido definido en el scope '{varScope}'"
                    if var.lower() == "not":
                        if var_type.lower() != "bool":
                            return f"La operacion '{var}' no es valida para variables de tipo '{var_type}'"
                        else:
                            return None

                return f"Las variables '{alphanum}' deben ser del mismo tipo '{var_type}'"

        return None

    def visit_expr_node(self, node):
        

        # Verifica while loops e ifs
        if node.children[0].val == "if" or node.children[0].val == "while":

            return self.check_comparisons(node)

        # methodcall sin parametros
        if len(node.children) == 3 and node.children[1].val == "(" and node.children[2].val == ")":
            methodName = node.children[0].val
            nodeScope = self.getClassDefineParent(node)
            for symbol in self.symbol_table.symbols:
                if symbol.name == methodName and symbol.id_type == "Method" and symbol.scope.startswith(nodeScope):
                    return None
            
            return f"El metodo '{methodName}' no ha sido definido en el scope '{nodeScope}'"
        
        # methodcall con parametros u operacion IO o return
        elif len(node.children) == 4 and node.children[1].val == "(" and node.children[3].val == ")":
            methodName = node.children[0].val
            nodeScope = self.getClassDefineParent(node)
            # print("mehtodName: ", methodName)
            IOmethods = ["out_int", "out_string", "in_int", "in_string", "out_bool", "in_bool"]

            if methodName == "return":

                # print("nodeScope: ", nodeScope)
                # print("methodName: ", methodName)

                node_value = self.getExprChildren(node.children[2])

                methodScope = self.getMethodParent(node)

                wholeScope = nodeScope + "." + methodScope

                # print("wholeScope: ", wholeScope)

                # print("node_value: ", node_value)

                methodType = None

                methodreturnType = None

                node_value_string =  " ".join(node_value)

                if "+" in node_value_string:
                    lista_temp = node_value_string.split("+")
                    # print("lista_temp: ", lista_temp)
                    lista_tipos = []
                    for item in lista_temp:
                        
                        item = item.strip(" ")

                        if item in self.names:
                            symbolIo2 = self.symbol_table.lookup(item)
                            lista_tipos.append(symbolIo2.data_type)
                        else:
                            lista_tipos.append(self.tokenDict[item])
                        
                    if all(value.lower() == lista_tipos[0].lower() for value in lista_tipos):

                        symbolType = lista_tipos[0]

                        return None
                    
                    else:

                        return f"Los parametros de '{methodName}' deben ser del mismo tipo"

                for symbol_temp in self.symbol_table.symbols:

                    # print("symbol_temp.name: ", symbol_temp.name)
                    # print("symbol_temp.scope: ", symbol_temp.scope)
                    # print(symbol_temp.name == methodName)
                    # print(symbol_temp.scope == wholeScope)

                    if str(symbol_temp.name) == str(methodName) and str(symbol_temp.scope) == str(wholeScope):

                        methodType = symbol_temp.value
                    
                    if symbol_temp.name == methodScope and symbol_temp.scope == nodeScope and symbol_temp.id_type == "Method":

                        methodreturnType = symbol_temp.data_type



                # print("methodType: ", methodType)
                # print("methodreturnType: ", methodreturnType)

                method_type_2 = None
                if methodType in self.names:

                    method_type_2 = self.symbol_table.lookup_all(methodType).data_type

                    if method_type_2.lower() != methodreturnType.lower():

                        return f"El metodo {methodScope} debe retornar un '{methodreturnType}' no un '{method_type_2}'"

                else:

                    method_type_2 = self.tokenDict[methodType]

                    if methodType == "self":

                        if methodreturnType != "SELF_TYPE":

                            return f"El metodo {methodScope} debe retornar un '{methodreturnType}' no un '{methodType}'"

                    else:

                        if method_type_2.lower() != methodreturnType.lower():

                            return f"El metodo {methodScope} debe retornar un '{methodreturnType}' no un '{method_type_2}'"


                # print(method_type_2)   

                return None

            # Verifica que el metodo este definido en el scope
            for symbol in self.symbol_table.symbols:
               
                # Verifica que el metodo este definido en el scope actual

                if methodName not in IOmethods:
                    
                    if symbol.name == methodName and symbol.id_type == "Method" and symbol.scope.startswith(nodeScope):

                        # Queremos revisar que los parametros definidos sean los correctos

                        # Para este metodo

                        # test(x : Int) : Int {
                        #     out_int(2)
                        # };

                        # Estamos revisando que la llamada "test("1");" sea correcta
                        # 

                        # Guardamos los parametros del metodo en una lista

                        # print(">methodName: ", methodName)

                        parameters = []
                        for symbol in self.symbol_table.symbols:
                            if methodName in symbol.scope and symbol.id_type == "Parameter" and symbol.scope.startswith(nodeScope):
                                parameters.append(symbol.data_type)    

                        # print(">parameters: ", parameters)  

                        # Verifica que los parametros de la llamada sean los correctos

                        for symbol in self.symbol_table.symbols:

                            # Se verifica para un method call

                            if symbol.name == methodName and symbol.id_type == "MethodCall":
                                if symbol.value in self.names:
                                    symbol = self.symbol_table.lookup(symbol.value)
                                    symbolType = symbol.data_type
                                else:
                                    # print(symbol)
                                    symbolType = self.tokenDict[symbol.value]
                                if symbol.name in IOmethods:
                                    pass
                                else:
                                    # print(len(parameters)) 
                                    if len(parameters) == 1 and parameters[0].lower() == symbolType.lower():
                                        return None
                                    else:
                                        return f"El metodo '{methodName}' debe recibir {len(parameters)} parametro(s) de tipo '{', '.join(parameters)}'"

                            # Se verifica para un Procedure call

                            elif symbol.name == methodName and symbol.id_type == "Procedure":
                               
                                if symbol.value in self.names:
                                    symbol = self.symbol_table.lookup(symbol.value)
                                    symbolType = symbol.data_type
                                else:
                                    symbolType = self.tokenDict[symbol.value]
                                if symbol.name in IOmethods:
                                    pass
                                else:
                                    # print(len(parameters)) 
                                    if len(parameters) == 1 and parameters[0].lower() == symbolType.lower():
                                        return None
                                    else:
                                        return f"El metodo '{methodName}' debe recibir {len(parameters)} parametro(s) de tipo '{', '.join(parameters)}'"


                        return None
 




                # Si son parte del IO revisa que el parametro sea el correcto
                
                else:
                    for symbol3 in self.symbol_table.symbols:
                        if symbol3.name == methodName:

                            if symbol3.value in self.names:
                                symbolIo2 = self.symbol_table.lookup(symbol3.value)
                                symbolType = symbolIo2.data_type
                            else:
                                # print(symbol)
                                if "+" in symbol3.value:
                                    lista_temp = symbol3.value.split("+")
                                    lista_tipos = []
                                    for item in lista_temp:
                                        
                                        item = item.strip(" ")

                                        if item in self.names:
                                            symbolIo2 = self.symbol_table.lookup(item)
                                            lista_tipos.append(symbolIo2.data_type)
                                        else:
                                            lista_tipos.append(self.tokenDict[item])
                                        
                                    if all(value.lower() == lista_tipos[0].lower() for value in lista_tipos):

                                        symbolType = lista_tipos[0]
                                    
                                    else:

                                        return f"Los parametros de '{methodName}' deben ser del mismo tipo"

                                else:
                                    symbolType = self.tokenDict[symbol3.value]
                            
                            if symbol3.name == IOmethods[0] or symbol3.name == IOmethods[2]:
                                if symbolType.lower() != "int":
                                    return f"El metodo '{methodName}' debe recibir un parametro de tipo 'int'"

                            elif symbol3.name == IOmethods[1] or symbol3.name == IOmethods[3]:
                                if symbolType.lower() != "string":
                                    return f"El metodo '{methodName}' debe recibir un parametro de tipo 'string'"
                            
                            elif symbol3.name == IOmethods[4] or symbol3.name == IOmethods[5]:
                                if symbolType.lower() != "bool":
                                    return f"El metodo '{methodName}' debe recibir un parametro de tipo 'bool'"
                      
                    # symbol2 = self.symbol_table.lookup_all("Main")
                    try:
                        if symbol.name == "IO":
                            return None
                    except:
                        pass

            # Si termina el for sin retornar es porque no encontro el metodo (No esta definido en el scope)        
            if methodName == "String" or methodName == "Bool" or methodName == "Int":
                return f"No se permite el casteo explicito {methodName}"
            else:
                return f"El metodo '{methodName}' no ha sido definido en el scope '{nodeScope}'"
        
        # Methodcall con uno o mas varios parametros
        elif len(node.children) > 4 and node.children[1].val == "(" and node.children[-1].val == ")":
            methodName = node.children[0].val

            nodeScope = self.getClassDefineParent(node)

            #revisar que los parametros si sean los correctos
            parameters = []

            
            for symbol in self.symbol_table.symbols:
                if methodName in symbol.scope and symbol.id_type == "Parameter" and symbol.scope.startswith(nodeScope):
                    parameters.append(symbol.data_type)

            # No existe ese metodo en el scope
            if len(parameters) == 0:

                return f"El metodo '{methodName}' no ha sido definido en el scope '{nodeScope}'"

            for symbol in self.symbol_table.symbols:
                if symbol.name == methodName and symbol.id_type == "MethodCall":
                    separate_parameters = symbol.value.split(",")
                    typeParameters = []
                    if len(parameters) == len(separate_parameters):
                        # print(separate_parameters)

                        for param in separate_parameters:
                            if param in self.names:
                                symbol = self.symbol_table.lookup(param)
                                typeParameters.append(symbol.data_type)
                            else:
                                typeParameters.append(self.tokenDict[param])
                        
                        for i in range(len(parameters)):
                            if parameters[i].lower() != typeParameters[i].lower():
                                return f"El metodo '{methodName}' debe recibir {len(parameters)} parametro(s) de tipo '{', '.join(parameters)}'"
                    else:
                        return f"El metodo '{methodName}' debe recibir {len(parameters)} parametro(s) de tipo '{', '.join(parameters)}'"

    # HELPER METHODS

    # Agarramos el scope de la clase
    def getClassDefineParent(self, node):
        if node.val == "classDefine":
            return node.children[1].val
        
        return self.getClassDefineParent(node.parent)
    
    # Agarramos el scope del metodo
    def getMethodParent(self, node):
        if node.val == "method":
            return node.children[0].val
        return self.getMethodParent(node.parent)

    # Agarramos los hijos de un nodo expr
    def getExprChildren(self, node, child_values=None):
        if child_values is None:
            child_values = []  # Initialize the list only in the initial call
        
        for child in node.children:
            if child.val == "expr":
                self.getExprChildren(child, child_values)  # Pass the existing list to the recursive call
            else:
                child_values.append(child.val)
        
        return child_values
    
    # Verifica que las comparaciones sean validas
    def check_comparisons(self, node):

        primera_comparacion = node.children[1]
        expresion = self.getExprChildren(primera_comparacion)
        variables_comparadas = [expresion[0], expresion[2]]

        tipos_datos_comparados = []

        for variable in variables_comparadas:

            # Si es una variable no declarada

            if variable in self.names:

                symbol_temporal = self.symbol_table.lookup(variable)

                tipos_datos_comparados.append(symbol_temporal.data_type)
            
            # Si es un token

            else:

                tipo_dato = self.tokenDict[variable]

                tipos_datos_comparados.append(tipo_dato)

        if tipos_datos_comparados[0].lower() != tipos_datos_comparados[1].lower():

            if tipos_datos_comparados[0].lower() in ["int","false","true"] and tipos_datos_comparados[1].lower() in ["int","false","true"]:

                return None

            return f"La comparación '{tipos_datos_comparados[0].lower()} con {tipos_datos_comparados[1].lower()}' no es válida"


        return None

    # Revisa que no se declaren dos veces el mismo identificador
    def checkDoubleDeclarations(self):

        poissbleErrors = []

        lista_tuplas = []

        for symbol in self.symbol_table.symbols:

            if (symbol.name, symbol.scope) in lista_tuplas:

                if symbol.id_type == "MethodCall" or symbol.id_type == "Procedure":

                    pass
                
                else:

                    poissbleErrors.append(f"ERROR SEMÁNTICO: El identificador '{symbol.name}' ya ha sido declarado en el scope '{symbol.scope}': Línea {symbol.line}")
            
            else:

                lista_tuplas.append((symbol.name, symbol.scope))
        
        return poissbleErrors


class SemanticAnalyzer:
    def __init__(self, parse_tree, symbol_table, tokenDict):
        self.parse_tree = parse_tree
        self.symbol_table = symbol_table
        self.tokenDict = tokenDict
        self.visitor = SemanticVisitor(self.symbol_table, self.tokenDict)
        self.errors = []

    def analyze(self):
        self.traverse_tree(self.parse_tree.root)

        checkDoubleDeclarations_errors = self.visitor.checkDoubleDeclarations()

        if checkDoubleDeclarations_errors:
            for error in checkDoubleDeclarations_errors:
                self.errors.append(error)
        
        self.display_errors()



    def traverse_tree(self, node):
        if node is not None:
            method_name = "visit_" + node.val.lower() + "_node"
            if hasattr(self.visitor, method_name):
                visit_method = getattr(self.visitor, method_name)
                error_message = visit_method(node)
                if error_message:
                    line_number = node.line
                    self.report_error(error_message, line_number)
            for child in node.children:
                self.traverse_tree(child)

    def report_error(self, message, line_number):
        error = f"{message}: Línea {line_number}"
        self.errors.append("ERROR SEMÁNTICO: " +  error)

    def display_errors(self):
        if self.errors:
            print("\nERRORES SEMÁNTICOS DETECTADOS:")
            for error in self.errors:
                print(error)
        else:
            print("No se encontraron errores semánticos.")

class MyErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if "extraneous input" not in msg:
            error_message = f"ERROR SINTÁCTICO: El problema es: {msg} : Línea {line}"
            self.errors.append(error_message)

