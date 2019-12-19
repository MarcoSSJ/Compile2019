# Generated from tinyc.g4 by ANTLR 4.7.2
from antlr4 import *
from parser_.tinycLexer import tinycLexer
from parser_.tinycListener import tinycListener
from parser_.tinycParser import tinycParser
from parser_.tinycVisitor import  tinycVisitor

# This class defines a complete generic visitor for a parse tree produced by tinycParser.

class c2llvmVisitor(tinycVisitor):

    def __init__(self):
        pass
    # Visit a parse tree produced by tinycParser#program.
    def visitProgram(self, ctx:tinycParser.ProgramContext):
        print('visit program')
        total = ctx.getChildCount()
        for index in range(total):
            # print(ctx.getChild(index).getRuleIndex())
            self.visit(ctx.getChild(index))
        return


    # Visit a parse tree produced by tinycParser#include.
    def visitInclude(self, ctx:tinycParser.IncludeContext):
        print('visit include')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#translationUnit.
    def visitTranslationUnit(self, ctx:tinycParser.TranslationUnitContext):
        print('visit trans unit')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#function.
    def visitFunction(self, ctx:tinycParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:tinycParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#compoundStatement.
    def visitCompoundStatement(self, ctx:tinycParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#compoundUnit.
    def visitCompoundUnit(self, ctx:tinycParser.CompoundUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#declaration.
    def visitDeclaration(self, ctx:tinycParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#initDeclaration.
    def visitInitDeclaration(self, ctx:tinycParser.InitDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#initDeclarator.
    def visitInitDeclarator(self, ctx:tinycParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#declarator.
    def visitDeclarator(self, ctx:tinycParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:tinycParser.ParameterTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#parameterList.
    def visitParameterList(self, ctx:tinycParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:tinycParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#statement.
    def visitStatement(self, ctx:tinycParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#expression.
    def visitExpression(self, ctx:tinycParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:tinycParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#postfixExpression.
    def visitPostfixExpression(self, ctx:tinycParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:tinycParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)

