import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from nodes.Program import Program
from visitors.InterpeterVisitor import InterpreterVisitor


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    ast_tree: Program = ExprVisitor().visit(tree)
    print(ast_tree.expressions)

    try:
        interpeter = InterpreterVisitor()

        # ast_tree.accept(interpeter)

        interpeter.visit_program(ast_tree)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv)
