from parser_.tinycLexer import tinycLexer
from parser_.tinycListener import tinycListener
from parser_.tinycParser import tinycParser
from precompile.preCompileParser import preCompileParser
from precompile.preCompileLexer import preCompileLexer
from precompile.preCompileVisitor import preCompileVisitor
from antlr4 import *
import llvmlite.ir as ir
from visitor import c2llvmVisitor
from preCompiler import preCompiler
import re
from preprocess.CmacrosVisitor import CmacrosVisitor
from preprocess.CmacrosLexer import CmacrosLexer
from preprocess.CmacrosParser import CmacrosParser
from macro import MacroVisitor

def preCompile(filename, output):
    input_stream = FileStream(filename)
    lexer = CmacrosLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CmacrosParser(token_stream)
    # Entry point in the json g4 grammar: json
    tree = parser.program()
    my_visitor =MacroVisitor()
    # walker = ParseTreeWalker()
    # walker.walk(my_listener, tree)
    my_visitor.visit(tree)
    # print('my_visitor.define', my_visitor.define)
    # output_str = str(input_stream)
    # for cname, define in my_visitor.define:
    #     # replace the define
    #     str_re = re.compile(cname)
    #     output_str = str_re.sub(define, output_str)
    # output_str = re.compile('#define.*\n').sub('', output_str)
    # with open(output, "w") as f:
    #     f.write(output_str)

    # input_stream = FileStream(filename)
    # lexer = tinycLexer(input_stream)
    # token_stream = CommonTokenStream(lexer)
    # parser = tinycParser(token_stream)
    # # Entry point in the json g4 grammar: json
    # tree = parser.program()
    # my_visitor = preCompiler()
    # # walker = ParseTreeWalker()
    # # walker.walk(my_listener, tree)
    # my_visitor.visit(tree)
    # print('my_visitor.define', my_visitor.define)
    # output_str = str(input_stream)
    # for cname, define in my_visitor.define:
    #     # replace the define
    #     str_re = re.compile(cname)
    #     output_str = str_re.sub(define, output_str)
    # output_str = re.compile('#define.*\n').sub('', output_str)
    # with open(output, "w") as f:
    #     f.write(output_str)

def main(filename, output):
    # input_stream = FileStream('temp.c')
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


filename = 'test/palindrome.c'
temp = 'temp.c'
output = 'output.ll'
preCompile(filename, temp)
# main(temp, output)
