from antlr4 import *
from precompile.preCompileLexer import preCompileLexer
from precompile.preCompileListener import preCompileListener
from precompile.preCompileParser import preCompileParser
from precompile.preCompileVisitor import preCompileVisitor
from util import *
from SymbolTable import SymbolTable
# This class defines a complete generic visitor for a parse tree produced by tinycParser.


class preCompiler(preCompileVisitor):

    def __init__(self):
        super(preCompiler, self).__init__()
        self.module = ir.Module()
        self.symbol_table = SymbolTable()
        self.define = []
        pass

    # Visit a parse tree produced by tinycParser#program.
    def visitProgram(self, ctx:tinycParser.ProgramContext):
        total = ctx.getChildCount()
        print('visit program', total, ctx, ctx.getText())
        for index in range(total):
            print('\n\n++ctx.getChild(index):', ctx.getChild(index))
            self.visit(ctx.getChild(index))
        return

    # Visit a parse tree produced by tinycParser#include.
    def visitInclude(self, ctx:tinycParser.IncludeContext):
        print('visit include', ctx.getChild(2).getText())
        return self.visitChildren(ctx)

    def visitDefine(self, ctx:preCompileParser.DefineContext):
        print('visit define', ctx.getText(), ctx.getChildren())
        total = ctx.getChildCount()
        for index in range(total):
            print(index, ctx.getChild(index))
        self.define.append((ctx.getChild(1).getText(), ctx.getChild(2).getText()))
        print('define', self.define)
        return self.visitChildren(ctx)
