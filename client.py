from antlr4 import *
from antlrSA.SemanticAnalysisLexer import SemanticAnalysisLexer
from antlrSA.SemanticAnalysisParser import SemanticAnalysisParser
from antlrSA.SemanticAnalysisListener import SemanticAnalysisListener
from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener



class functionReturn(SemanticAnalysisListener):
    def enterFunc_def(self, ctx):
        data_types = ctx.data_type()  # Obtener la lista de tipos de datos
        func_type = data_types[0].getText()  # Obtener el primer tipo de dato (tipo de retorno)
        return_expr = ctx.expr().getText()  # Obtener la expresión de retorno
        if func_type != return_expr:
            print(f"Error: Return type '{return_expr}' does not match function type '{func_type}'")



def main(file_path):
    input_stream = FileStream(file_path)
    lexer = SemanticAnalysisLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SemanticAnalysisParser(stream)
    tree = parser.program()

    listener = functionReturn()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)



if __name__ == '__main__':
    main('test_incorrect_3.txt')
