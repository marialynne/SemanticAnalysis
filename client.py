from _ast import Expression

from antlr4 import *
from antlrSA.SemanticAnalysisLexer import SemanticAnalysisLexer
from antlrSA.SemanticAnalysisParser import SemanticAnalysisParser
from antlrSA.SemanticAnalysisListener import SemanticAnalysisListener
from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column}: {msg}")

class VariableDeclarationListener(SemanticAnalysisListener):
    def _init_(self):
        self.variables = set()

    def enterVarDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        self.variables.add(var_name)

    def enterVariable(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            print(f"Error: Variable '{var_name}' used without being declared.")


class ArithmeticExpressionListener(SemanticAnalysisListener):
    def _init_(self):
        pass

    def enterMult(self, ctx: SemanticAnalysisParser.MultContext):
        # Verificar que los operandos de la multiplicación sean numéricos
        left_expr_type = ctx.expr(0).dataType().getText()
        right_expr_type = ctx.expr(1).dataType().getText()
        if left_expr_type != "int" or right_expr_type != "int":
            print("Error: Multiplication operands must be of type 'int'.")

    def enterDiv(self, ctx: SemanticAnalysisParser.DivContext):
        # Verificar que los operandos de la división sean numéricos y que el divisor no sea cero
        left_expr_type = ctx.expr(0).dataType().getText()
        right_expr_type = ctx.expr(1).dataType().getText()
        if left_expr_type != "int" or right_expr_type != "int":
            print("Error: Division operands must be of type 'int'.")
        if ctx.expr(1).getText() == "0":
            print("Error: Division by zero.")

    def enterSqrt(self, ctx: SemanticAnalysisParser.SqrtContext):
        # Verificar que el operando de la raíz cuadrada sea numérico y no negativo
        expr_type = ctx.expr().dataType().getText()
        if expr_type != "int" and expr_type != "float":
            print("Error: Operand of sqrt must be of type 'int' or 'float'.")
        if ctx.expr().getText() == "0":
            print("Error: Cannot take square root of zero.")

    def enterPower(self, ctx: SemanticAnalysisParser.PowerContext):
        # Verificar que los operandos de la potenciación sean numéricos
        left_expr_type = ctx.expr(0).dataType().getText()
        right_expr_type = ctx.expr(1).dataType().getText()
        if left_expr_type != "int" or right_expr_type != "int":
            print("Error: Power operands must be of type 'int'.")



class FunctionReturnListener(SemanticAnalysisListener):
    def _init_(self):
        self.functions = {}

    def enterFunctionDeclaration(self, ctx):
        func_name = ctx.ID().getText()
        return_type = ctx.dataType().getText()
        self.functions[func_name] = return_type

    def enterReturnStatement(self, ctx):
        func_name = ctx.ID().getText()
        return_expr_type = ctx.expr().dataType().getText()
        if func_name in self.functions:
            declared_return_type = self.functions[func_name]
            if return_expr_type != declared_return_type:
                print(f"Error: Return type mismatch in function '{func_name}'. Expected '{declared_return_type}', got '{return_expr_type}'.")

def main(file_path):
    input_stream = FileStream(file_path)
    lexer = SemanticAnalysisLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SemanticAnalysisParser(stream)
    tree = parser.program()

    # Crear e instanciar los listeners de validación
    var_listener = VariableDeclarationListener()
    arith_expr_listener = ArithmeticExpressionListener()
    return_listener = FunctionReturnListener()

    # Recorrer el árbol con los listeners
    walker = ParseTreeWalker()
    walker.walk(var_listener, tree)
    walker.walk(arith_expr_listener, tree)
    walker.walk(return_listener, tree)

if __name__ == '__main__':
    main('test_incorrect_2.txt')