from parser_.tinycLexer import tinycLexer
from parser_.tinycListener import tinycListener
from parser_.tinycParser import tinycParser
from antlr4 import *
import llvmlite.ir as ir
from visitor import c2llvmVisitor

def main(filename, output):
    input_stream = FileStream(filename)
    lexer = tinycLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = tinycParser(token_stream)
    # Entry point in the json g4 grammar: json
    tree = parser.program()
    my_visitor = c2llvmVisitor()
    # walker = ParseTreeWalker()
    # walker.walk(my_listener, tree)
    my_visitor.visit(tree)
    with open(output, "w") as f:
        f.write(repr(my_visitor.module))

main('test\iterationhelloworld.c','output.ll')