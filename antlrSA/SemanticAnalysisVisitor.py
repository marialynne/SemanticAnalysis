# Generated from /Users/marialynne/PycharmProjects/SemanticAnalysis/antlrSA/SemanticAnalysis.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SemanticAnalysisParser import SemanticAnalysisParser
else:
    from SemanticAnalysisParser import SemanticAnalysisParser

# This class defines a complete generic visitor for a parse tree produced by SemanticAnalysisParser.

class SemanticAnalysisVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SemanticAnalysisParser#program.
    def visitProgram(self, ctx:SemanticAnalysisParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#constDecl.
    def visitConstDecl(self, ctx:SemanticAnalysisParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#varDecl.
    def visitVarDecl(self, ctx:SemanticAnalysisParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#assign.
    def visitAssign(self, ctx:SemanticAnalysisParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#if_else.
    def visitIf_else(self, ctx:SemanticAnalysisParser.If_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#while.
    def visitWhile(self, ctx:SemanticAnalysisParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#functionCall.
    def visitFunctionCall(self, ctx:SemanticAnalysisParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#func_def.
    def visitFunc_def(self, ctx:SemanticAnalysisParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#ident.
    def visitIdent(self, ctx:SemanticAnalysisParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#int.
    def visitInt(self, ctx:SemanticAnalysisParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#float_dt.
    def visitFloat_dt(self, ctx:SemanticAnalysisParser.Float_dtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#string_dt.
    def visitString_dt(self, ctx:SemanticAnalysisParser.String_dtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#add.
    def visitAdd(self, ctx:SemanticAnalysisParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#sub.
    def visitSub(self, ctx:SemanticAnalysisParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#mult.
    def visitMult(self, ctx:SemanticAnalysisParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#string.
    def visitString(self, ctx:SemanticAnalysisParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#integer.
    def visitInteger(self, ctx:SemanticAnalysisParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#float.
    def visitFloat(self, ctx:SemanticAnalysisParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#div.
    def visitDiv(self, ctx:SemanticAnalysisParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#equal.
    def visitEqual(self, ctx:SemanticAnalysisParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#sqrt.
    def visitSqrt(self, ctx:SemanticAnalysisParser.SqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#lessEq.
    def visitLessEq(self, ctx:SemanticAnalysisParser.LessEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#greaterEq.
    def visitGreaterEq(self, ctx:SemanticAnalysisParser.GreaterEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#id.
    def visitId(self, ctx:SemanticAnalysisParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SemanticAnalysisParser#power.
    def visitPower(self, ctx:SemanticAnalysisParser.PowerContext):
        return self.visitChildren(ctx)



del SemanticAnalysisParser