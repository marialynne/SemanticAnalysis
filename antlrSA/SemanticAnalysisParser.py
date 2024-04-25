# Generated from /Users/marialynne/PycharmProjects/SemanticAnalysis/antlrSA/SemanticAnalysis.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,180,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,5,2,45,8,2,10,2,12,2,48,9,2,1,2,1,2,1,2,1,2,5,2,54,8,2,10,2,
        12,2,57,9,2,1,2,3,2,60,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,70,
        8,2,10,2,12,2,73,9,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,81,8,2,1,2,1,2,
        1,2,5,2,86,8,2,10,2,12,2,89,9,2,3,2,91,8,2,1,2,1,2,3,2,95,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,107,8,3,10,3,12,3,110,
        9,3,3,3,112,8,3,1,3,1,3,1,3,1,3,5,3,118,8,3,10,3,12,3,121,9,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,132,8,4,1,5,1,5,1,5,3,5,137,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,149,8,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,5,6,175,8,6,10,6,12,6,178,9,6,1,6,0,1,12,
        7,0,2,4,6,8,10,12,0,0,205,0,19,1,0,0,0,2,31,1,0,0,0,4,94,1,0,0,0,
        6,96,1,0,0,0,8,128,1,0,0,0,10,136,1,0,0,0,12,148,1,0,0,0,14,18,3,
        2,1,0,15,18,3,4,2,0,16,18,3,6,3,0,17,14,1,0,0,0,17,15,1,0,0,0,17,
        16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,1,1,0,0,
        0,21,19,1,0,0,0,22,23,5,17,0,0,23,24,3,10,5,0,24,25,3,8,4,0,25,26,
        5,1,0,0,26,32,1,0,0,0,27,28,3,10,5,0,28,29,3,8,4,0,29,30,5,1,0,0,
        30,32,1,0,0,0,31,22,1,0,0,0,31,27,1,0,0,0,32,3,1,0,0,0,33,34,3,12,
        6,0,34,35,5,2,0,0,35,36,3,12,6,0,36,37,5,1,0,0,37,95,1,0,0,0,38,
        39,5,21,0,0,39,40,5,3,0,0,40,41,3,12,6,0,41,42,5,4,0,0,42,46,5,5,
        0,0,43,45,3,4,2,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,59,5,6,0,0,50,51,5,22,0,0,
        51,55,5,5,0,0,52,54,3,4,2,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,
        0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,60,5,6,0,0,59,
        50,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,1,0,0,62,95,1,0,0,
        0,63,64,5,23,0,0,64,65,5,3,0,0,65,66,3,12,6,0,66,67,5,4,0,0,67,71,
        5,5,0,0,68,70,3,4,2,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,6,0,0,75,76,5,
        1,0,0,76,95,1,0,0,0,77,78,5,26,0,0,78,90,5,3,0,0,79,81,5,26,0,0,
        80,79,1,0,0,0,80,81,1,0,0,0,81,91,1,0,0,0,82,87,5,26,0,0,83,84,5,
        7,0,0,84,86,5,26,0,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,
        88,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,90,80,1,0,0,0,90,82,1,0,0,
        0,91,92,1,0,0,0,92,93,5,4,0,0,93,95,5,1,0,0,94,33,1,0,0,0,94,38,
        1,0,0,0,94,63,1,0,0,0,94,77,1,0,0,0,95,5,1,0,0,0,96,97,5,24,0,0,
        97,98,3,10,5,0,98,99,5,26,0,0,99,111,5,3,0,0,100,101,3,10,5,0,101,
        108,3,8,4,0,102,103,5,7,0,0,103,104,3,10,5,0,104,105,3,8,4,0,105,
        107,1,0,0,0,106,102,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,
        109,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,111,100,1,0,0,0,111,
        112,1,0,0,0,112,113,1,0,0,0,113,114,5,4,0,0,114,119,5,5,0,0,115,
        118,3,4,2,0,116,118,3,2,1,0,117,115,1,0,0,0,117,116,1,0,0,0,118,
        121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,
        119,1,0,0,0,122,123,5,25,0,0,123,124,3,12,6,0,124,125,5,1,0,0,125,
        126,5,6,0,0,126,127,5,1,0,0,127,7,1,0,0,0,128,131,5,26,0,0,129,130,
        5,2,0,0,130,132,3,12,6,0,131,129,1,0,0,0,131,132,1,0,0,0,132,9,1,
        0,0,0,133,137,5,18,0,0,134,137,5,19,0,0,135,137,5,20,0,0,136,133,
        1,0,0,0,136,134,1,0,0,0,136,135,1,0,0,0,137,11,1,0,0,0,138,139,6,
        6,-1,0,139,140,5,8,0,0,140,141,5,3,0,0,141,142,3,12,6,0,142,143,
        5,4,0,0,143,149,1,0,0,0,144,149,5,26,0,0,145,149,5,27,0,0,146,149,
        5,28,0,0,147,149,5,29,0,0,148,138,1,0,0,0,148,144,1,0,0,0,148,145,
        1,0,0,0,148,146,1,0,0,0,148,147,1,0,0,0,149,176,1,0,0,0,150,151,
        10,12,0,0,151,152,5,9,0,0,152,175,3,12,6,13,153,154,10,11,0,0,154,
        155,5,10,0,0,155,175,3,12,6,12,156,157,10,10,0,0,157,158,5,11,0,
        0,158,175,3,12,6,11,159,160,10,9,0,0,160,161,5,12,0,0,161,175,3,
        12,6,10,162,163,10,8,0,0,163,164,5,13,0,0,164,175,3,12,6,9,165,166,
        10,7,0,0,166,167,5,14,0,0,167,175,3,12,6,8,168,169,10,6,0,0,169,
        170,5,15,0,0,170,175,3,12,6,7,171,172,10,5,0,0,172,173,5,16,0,0,
        173,175,3,12,6,6,174,150,1,0,0,0,174,153,1,0,0,0,174,156,1,0,0,0,
        174,159,1,0,0,0,174,162,1,0,0,0,174,165,1,0,0,0,174,168,1,0,0,0,
        174,171,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,
        177,13,1,0,0,0,178,176,1,0,0,0,20,17,19,31,46,55,59,71,80,87,90,
        94,108,111,117,119,131,136,148,174,176
    ]

class SemanticAnalysisParser ( Parser ):

    grammarFileName = "SemanticAnalysis.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'('", "')'", "'{'", "'}'", 
                     "','", "'sqrt'", "'**'", "'*'", "'/'", "'+'", "'-'", 
                     "'=='", "'>='", "'<='", "'const'", "'int'", "'float'", 
                     "'str'", "'if'", "'else'", "'while'", "'func'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CONST", "INT", "FLOAT", "STRING", "IF", 
                      "ELSE", "WHILE", "FUNC", "RETURN", "ID", "INTEGER", 
                      "DEC", "STR", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_statement = 2
    RULE_function = 3
    RULE_ident = 4
    RULE_data_type = 5
    RULE_expr = 6

    ruleNames =  [ "program", "declaration", "statement", "function", "ident", 
                   "data_type", "expr" ]

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
    CONST=17
    INT=18
    FLOAT=19
    STRING=20
    IF=21
    ELSE=22
    WHILE=23
    FUNC=24
    RETURN=25
    ID=26
    INTEGER=27
    DEC=28
    STR=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.DeclarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.StatementContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.StatementContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.FunctionContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.FunctionContext,i)


        def getRuleIndex(self):
            return SemanticAnalysisParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SemanticAnalysisParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1035862272) != 0):
                self.state = 17
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17, 18, 19, 20]:
                    self.state = 14
                    self.declaration()
                    pass
                elif token in [8, 21, 23, 26, 27, 28, 29]:
                    self.state = 15
                    self.statement()
                    pass
                elif token in [24]:
                    self.state = 16
                    self.function()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SemanticAnalysisParser.RULE_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConstDeclContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONST(self):
            return self.getToken(SemanticAnalysisParser.CONST, 0)
        def data_type(self):
            return self.getTypedRuleContext(SemanticAnalysisParser.Data_typeContext,0)

        def ident(self):
            return self.getTypedRuleContext(SemanticAnalysisParser.IdentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDecl" ):
                listener.enterConstDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDecl" ):
                listener.exitConstDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)


    class VarDeclContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def data_type(self):
            return self.getTypedRuleContext(SemanticAnalysisParser.Data_typeContext,0)

        def ident(self):
            return self.getTypedRuleContext(SemanticAnalysisParser.IdentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)



    def declaration(self):

        localctx = SemanticAnalysisParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = SemanticAnalysisParser.ConstDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(SemanticAnalysisParser.CONST)
                self.state = 23
                self.data_type()
                self.state = 24
                self.ident()
                self.state = 25
                self.match(SemanticAnalysisParser.T__0)
                pass
            elif token in [18, 19, 20]:
                localctx = SemanticAnalysisParser.VarDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.data_type()
                self.state = 28
                self.ident()
                self.state = 29
                self.match(SemanticAnalysisParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SemanticAnalysisParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionCallContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SemanticAnalysisParser.ID)
            else:
                return self.getToken(SemanticAnalysisParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(SemanticAnalysisParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.StatementContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class If_elseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(SemanticAnalysisParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.StatementContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(SemanticAnalysisParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_else" ):
                listener.enterIf_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_else" ):
                listener.exitIf_else(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_else" ):
                return visitor.visitIf_else(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = SemanticAnalysisParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = SemanticAnalysisParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.expr(0)
                self.state = 34
                self.match(SemanticAnalysisParser.T__1)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(SemanticAnalysisParser.T__0)
                pass

            elif la_ == 2:
                localctx = SemanticAnalysisParser.If_elseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(SemanticAnalysisParser.IF)
                self.state = 39
                self.match(SemanticAnalysisParser.T__2)
                self.state = 40
                self.expr(0)
                self.state = 41
                self.match(SemanticAnalysisParser.T__3)
                self.state = 42
                self.match(SemanticAnalysisParser.T__4)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1017118976) != 0):
                    self.state = 43
                    self.statement()
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 49
                self.match(SemanticAnalysisParser.T__5)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 50
                    self.match(SemanticAnalysisParser.ELSE)
                    self.state = 51
                    self.match(SemanticAnalysisParser.T__4)
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1017118976) != 0):
                        self.state = 52
                        self.statement()
                        self.state = 57
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 58
                    self.match(SemanticAnalysisParser.T__5)


                self.state = 61
                self.match(SemanticAnalysisParser.T__0)
                pass

            elif la_ == 3:
                localctx = SemanticAnalysisParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.match(SemanticAnalysisParser.WHILE)
                self.state = 64
                self.match(SemanticAnalysisParser.T__2)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(SemanticAnalysisParser.T__3)
                self.state = 67
                self.match(SemanticAnalysisParser.T__4)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1017118976) != 0):
                    self.state = 68
                    self.statement()
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 74
                self.match(SemanticAnalysisParser.T__5)
                self.state = 75
                self.match(SemanticAnalysisParser.T__0)
                pass

            elif la_ == 4:
                localctx = SemanticAnalysisParser.FunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.match(SemanticAnalysisParser.ID)
                self.state = 78
                self.match(SemanticAnalysisParser.T__2)
                self.state = 90
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==26:
                        self.state = 79
                        self.match(SemanticAnalysisParser.ID)


                    pass

                elif la_ == 2:
                    self.state = 82
                    self.match(SemanticAnalysisParser.ID)
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==7:
                        self.state = 83
                        self.match(SemanticAnalysisParser.T__6)
                        self.state = 84
                        self.match(SemanticAnalysisParser.ID)
                        self.state = 89
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass


                self.state = 92
                self.match(SemanticAnalysisParser.T__3)
                self.state = 93
                self.match(SemanticAnalysisParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SemanticAnalysisParser.RULE_function

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Func_defContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(SemanticAnalysisParser.FUNC, 0)
        def data_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.Data_typeContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.Data_typeContext,i)

        def ID(self):
            return self.getToken(SemanticAnalysisParser.ID, 0)
        def RETURN(self):
            return self.getToken(SemanticAnalysisParser.RETURN, 0)
        def expr(self):
            return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,0)

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.IdentContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.IdentContext,i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.StatementContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.StatementContext,i)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.DeclarationContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_def" ):
                listener.enterFunc_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_def" ):
                listener.exitFunc_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_def" ):
                return visitor.visitFunc_def(self)
            else:
                return visitor.visitChildren(self)



    def function(self):

        localctx = SemanticAnalysisParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            localctx = SemanticAnalysisParser.Func_defContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(SemanticAnalysisParser.FUNC)
            self.state = 97
            self.data_type()
            self.state = 98
            self.match(SemanticAnalysisParser.ID)
            self.state = 99
            self.match(SemanticAnalysisParser.T__2)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0):
                self.state = 100
                self.data_type()
                self.state = 101
                self.ident()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 102
                    self.match(SemanticAnalysisParser.T__6)
                    self.state = 103
                    self.data_type()
                    self.state = 104
                    self.ident()
                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 113
            self.match(SemanticAnalysisParser.T__3)
            self.state = 114
            self.match(SemanticAnalysisParser.T__4)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1019085056) != 0):
                self.state = 117
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 21, 23, 26, 27, 28, 29]:
                    self.state = 115
                    self.statement()
                    pass
                elif token in [17, 18, 19, 20]:
                    self.state = 116
                    self.declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(SemanticAnalysisParser.RETURN)
            self.state = 123
            self.expr(0)
            self.state = 124
            self.match(SemanticAnalysisParser.T__0)
            self.state = 125
            self.match(SemanticAnalysisParser.T__5)
            self.state = 126
            self.match(SemanticAnalysisParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SemanticAnalysisParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,0)


        def getRuleIndex(self):
            return SemanticAnalysisParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)




    def ident(self):

        localctx = SemanticAnalysisParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ident)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(SemanticAnalysisParser.ID)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 129
                self.match(SemanticAnalysisParser.T__1)
                self.state = 130
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SemanticAnalysisParser.RULE_data_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class String_dtContext(Data_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.Data_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(SemanticAnalysisParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_dt" ):
                listener.enterString_dt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_dt" ):
                listener.exitString_dt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_dt" ):
                return visitor.visitString_dt(self)
            else:
                return visitor.visitChildren(self)


    class Float_dtContext(Data_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.Data_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(SemanticAnalysisParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_dt" ):
                listener.enterFloat_dt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_dt" ):
                listener.exitFloat_dt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_dt" ):
                return visitor.visitFloat_dt(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(Data_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.Data_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SemanticAnalysisParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def data_type(self):

        localctx = SemanticAnalysisParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_data_type)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = SemanticAnalysisParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(SemanticAnalysisParser.INT)
                pass
            elif token in [19]:
                localctx = SemanticAnalysisParser.Float_dtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(SemanticAnalysisParser.FLOAT)
                pass
            elif token in [20]:
                localctx = SemanticAnalysisParser.String_dtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(SemanticAnalysisParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

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
            return SemanticAnalysisParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(SemanticAnalysisParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class IntegerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(SemanticAnalysisParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEC(self):
            return self.getToken(SemanticAnalysisParser.DEC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class DivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class SqrtContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqrt" ):
                listener.enterSqrt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqrt" ):
                listener.exitSqrt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqrt" ):
                return visitor.visitSqrt(self)
            else:
                return visitor.visitChildren(self)


    class LessEqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessEq" ):
                listener.enterLessEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessEq" ):
                listener.exitLessEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessEq" ):
                return visitor.visitLessEq(self)
            else:
                return visitor.visitChildren(self)


    class GreaterEqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterEq" ):
                listener.enterGreaterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterEq" ):
                listener.exitGreaterEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterEq" ):
                return visitor.visitGreaterEq(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SemanticAnalysisParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class PowerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SemanticAnalysisParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemanticAnalysisParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemanticAnalysisParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SemanticAnalysisParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = SemanticAnalysisParser.SqrtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 139
                self.match(SemanticAnalysisParser.T__7)
                self.state = 140
                self.match(SemanticAnalysisParser.T__2)
                self.state = 141
                self.expr(0)
                self.state = 142
                self.match(SemanticAnalysisParser.T__3)
                pass
            elif token in [26]:
                localctx = SemanticAnalysisParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(SemanticAnalysisParser.ID)
                pass
            elif token in [27]:
                localctx = SemanticAnalysisParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.match(SemanticAnalysisParser.INTEGER)
                pass
            elif token in [28]:
                localctx = SemanticAnalysisParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(SemanticAnalysisParser.DEC)
                pass
            elif token in [29]:
                localctx = SemanticAnalysisParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(SemanticAnalysisParser.STR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 174
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = SemanticAnalysisParser.PowerContext(self, SemanticAnalysisParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 150
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 151
                        self.match(SemanticAnalysisParser.T__8)
                        self.state = 152
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = SemanticAnalysisParser.MultContext(self, SemanticAnalysisParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 153
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 154
                        self.match(SemanticAnalysisParser.T__9)
                        self.state = 155
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = SemanticAnalysisParser.DivContext(self, SemanticAnalysisParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 156
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 157
                        self.match(SemanticAnalysisParser.T__10)
                        self.state = 158
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = SemanticAnalysisParser.AddContext(self, SemanticAnalysisParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 159
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 160
                        self.match(SemanticAnalysisParser.T__11)
                        self.state = 161
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = SemanticAnalysisParser.SubContext(self, SemanticAnalysisParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 163
                        self.match(SemanticAnalysisParser.T__12)
                        self.state = 164
                        self.expr(9)
                        pass

                    elif la_ == 6:
                        localctx = SemanticAnalysisParser.EqualContext(self, SemanticAnalysisParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 166
                        self.match(SemanticAnalysisParser.T__13)
                        self.state = 167
                        self.expr(8)
                        pass

                    elif la_ == 7:
                        localctx = SemanticAnalysisParser.GreaterEqContext(self, SemanticAnalysisParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 169
                        self.match(SemanticAnalysisParser.T__14)
                        self.state = 170
                        self.expr(7)
                        pass

                    elif la_ == 8:
                        localctx = SemanticAnalysisParser.LessEqContext(self, SemanticAnalysisParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 172
                        self.match(SemanticAnalysisParser.T__15)
                        self.state = 173
                        self.expr(6)
                        pass

             
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         




