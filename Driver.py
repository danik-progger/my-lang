import sys
from antlr4 import *
from interpreter.ExprLexer import ExprLexer
from interpreter.ExprParser import ExprParser
from interpreter.ExprVisitor import ExprVisitor
from interpreter.visitors.InterpeterVisitor import InterpreterVisitor
from interpreter.visitors.PrintVisitor import PrintVisitor


def main(argv):
    print(argv)
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    ast_tree = ExprVisitor().visit(tree)

    interpeter = InterpreterVisitor()
    interpeter.visit_program(ast_tree)

    printer = PrintVisitor()
    printer.visit_program(ast_tree)
    with open("tree.out", "w") as f:
        f.write(printer.str)


if __name__ == '__main__':
    main(sys.argv)
