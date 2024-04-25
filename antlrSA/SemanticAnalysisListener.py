# Generated from /Users/marialynne/PycharmProjects/SemanticAnalysis/antlrSA/SemanticAnalysis.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SemanticAnalysisParser import SemanticAnalysisParser
else:
    from SemanticAnalysisParser import SemanticAnalysisParser

# This class defines a complete listener for a parse tree produced by SemanticAnalysisParser.
class SemanticAnalysisListener(ParseTreeListener):

    # Enter a parse tree produced by SemanticAnalysisParser#program.
    def enterProgram(self, ctx:SemanticAnalysisParser.ProgramContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#program.
    def exitProgram(self, ctx:SemanticAnalysisParser.ProgramContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#constDecl.
    def enterConstDecl(self, ctx:SemanticAnalysisParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#constDecl.
    def exitConstDecl(self, ctx:SemanticAnalysisParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#varDecl.
    def enterVarDecl(self, ctx:SemanticAnalysisParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#varDecl.
    def exitVarDecl(self, ctx:SemanticAnalysisParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#assign.
    def enterAssign(self, ctx:SemanticAnalysisParser.AssignContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#assign.
    def exitAssign(self, ctx:SemanticAnalysisParser.AssignContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#if_else.
    def enterIf_else(self, ctx:SemanticAnalysisParser.If_elseContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#if_else.
    def exitIf_else(self, ctx:SemanticAnalysisParser.If_elseContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#while.
    def enterWhile(self, ctx:SemanticAnalysisParser.WhileContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#while.
    def exitWhile(self, ctx:SemanticAnalysisParser.WhileContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#functionCall.
    def enterFunctionCall(self, ctx:SemanticAnalysisParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#functionCall.
    def exitFunctionCall(self, ctx:SemanticAnalysisParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#func_def.
    def enterFunc_def(self, ctx:SemanticAnalysisParser.Func_defContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#func_def.
    def exitFunc_def(self, ctx:SemanticAnalysisParser.Func_defContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#ident.
    def enterIdent(self, ctx:SemanticAnalysisParser.IdentContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#ident.
    def exitIdent(self, ctx:SemanticAnalysisParser.IdentContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#int.
    def enterInt(self, ctx:SemanticAnalysisParser.IntContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#int.
    def exitInt(self, ctx:SemanticAnalysisParser.IntContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#float_dt.
    def enterFloat_dt(self, ctx:SemanticAnalysisParser.Float_dtContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#float_dt.
    def exitFloat_dt(self, ctx:SemanticAnalysisParser.Float_dtContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#string_dt.
    def enterString_dt(self, ctx:SemanticAnalysisParser.String_dtContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#string_dt.
    def exitString_dt(self, ctx:SemanticAnalysisParser.String_dtContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#add.
    def enterAdd(self, ctx:SemanticAnalysisParser.AddContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#add.
    def exitAdd(self, ctx:SemanticAnalysisParser.AddContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#sub.
    def enterSub(self, ctx:SemanticAnalysisParser.SubContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#sub.
    def exitSub(self, ctx:SemanticAnalysisParser.SubContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#mult.
    def enterMult(self, ctx:SemanticAnalysisParser.MultContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#mult.
    def exitMult(self, ctx:SemanticAnalysisParser.MultContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#string.
    def enterString(self, ctx:SemanticAnalysisParser.StringContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#string.
    def exitString(self, ctx:SemanticAnalysisParser.StringContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#integer.
    def enterInteger(self, ctx:SemanticAnalysisParser.IntegerContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#integer.
    def exitInteger(self, ctx:SemanticAnalysisParser.IntegerContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#float.
    def enterFloat(self, ctx:SemanticAnalysisParser.FloatContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#float.
    def exitFloat(self, ctx:SemanticAnalysisParser.FloatContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#div.
    def enterDiv(self, ctx:SemanticAnalysisParser.DivContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#div.
    def exitDiv(self, ctx:SemanticAnalysisParser.DivContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#equal.
    def enterEqual(self, ctx:SemanticAnalysisParser.EqualContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#equal.
    def exitEqual(self, ctx:SemanticAnalysisParser.EqualContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#sqrt.
    def enterSqrt(self, ctx:SemanticAnalysisParser.SqrtContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#sqrt.
    def exitSqrt(self, ctx:SemanticAnalysisParser.SqrtContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#lessEq.
    def enterLessEq(self, ctx:SemanticAnalysisParser.LessEqContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#lessEq.
    def exitLessEq(self, ctx:SemanticAnalysisParser.LessEqContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#greaterEq.
    def enterGreaterEq(self, ctx:SemanticAnalysisParser.GreaterEqContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#greaterEq.
    def exitGreaterEq(self, ctx:SemanticAnalysisParser.GreaterEqContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#id.
    def enterId(self, ctx:SemanticAnalysisParser.IdContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#id.
    def exitId(self, ctx:SemanticAnalysisParser.IdContext):
        pass


    # Enter a parse tree produced by SemanticAnalysisParser#power.
    def enterPower(self, ctx:SemanticAnalysisParser.PowerContext):
        pass

    # Exit a parse tree produced by SemanticAnalysisParser#power.
    def exitPower(self, ctx:SemanticAnalysisParser.PowerContext):
        pass




del SemanticAnalysisParser