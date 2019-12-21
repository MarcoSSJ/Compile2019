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

    # Visit a parse tree produced by preCompileParser#program.
    def visitProgram(self, ctx:preCompileParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#statement.
    def visitStatement(self, ctx:preCompileParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#preprocess.
    def visitPreprocess(self, ctx:preCompileParser.PreprocessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppChars.
    def visitPpChars(self, ctx:preCompileParser.PpCharsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppInclude.
    def visitPpInclude(self, ctx:preCompileParser.PpIncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppPragma.
    def visitPpPragma(self, ctx:preCompileParser.PpPragmaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppError.
    def visitPpError(self, ctx:preCompileParser.PpErrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppUndef.
    def visitPpUndef(self, ctx:preCompileParser.PpUndefContext):
        id = ctx.ID().getText()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppDefineVar.
    def visitPpDefineVar(self, ctx:preCompileParser.PpDefineVarContext):
        id = ctx.ID().getText()
        var = ctx.ppChars().getText()
        if var:
            try:
                self.symbol_table.addSymbol(id, var)
            except:
                raise Exception('redefine error')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppDefineFunc.
    def visitPpDefineFunc(self, ctx:preCompileParser.PpDefineFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppdfId.
    def visitPpdfId(self, ctx:preCompileParser.PpdfIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppdfiArguments.
    def visitPpdfiArguments(self, ctx:preCompileParser.PpdfiArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppdfiArgument.
    def visitPpdfiArgument(self, ctx:preCompileParser.PpdfiArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppdfChars.
    def visitPpdfChars(self, ctx:preCompileParser.PpdfCharsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppdfcId.
    def visitPpdfcId(self, ctx:preCompileParser.PpdfcIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppdfcNotId.
    def visitPpdfcNotId(self, ctx:preCompileParser.PpdfcNotIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppIfStatement.
    def visitPpIfStatement(self, ctx:preCompileParser.PpIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppisIfDef.
    def visitPpisIfDef(self, ctx:preCompileParser.PpisIfDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppisIfNdef.
    def visitPpisIfNdef(self, ctx:preCompileParser.PpisIfNdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#ppisStatement.
    def visitPpisStatement(self, ctx:preCompileParser.PpisStatementContext):
        return self.visitChildren(ctx)
