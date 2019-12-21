# Generated from preCompile.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .preCompileParser import preCompileParser
else:
    from preCompileParser import preCompileParser

# This class defines a complete generic visitor for a parse tree produced by preCompileParser.

class preCompileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by preCompileParser#program.
    def visitProgram(self, ctx:preCompileParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#include.
    def visitInclude(self, ctx:preCompileParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#define.
    def visitDefine(self, ctx:preCompileParser.DefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#translationUnit.
    def visitTranslationUnit(self, ctx:preCompileParser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#function.
    def visitFunction(self, ctx:preCompileParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:preCompileParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#compoundStatement.
    def visitCompoundStatement(self, ctx:preCompileParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#compoundUnit.
    def visitCompoundUnit(self, ctx:preCompileParser.CompoundUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#declaration.
    def visitDeclaration(self, ctx:preCompileParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#initDeclaration.
    def visitInitDeclaration(self, ctx:preCompileParser.InitDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#initDeclarator.
    def visitInitDeclarator(self, ctx:preCompileParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#initializer.
    def visitInitializer(self, ctx:preCompileParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#declarator.
    def visitDeclarator(self, ctx:preCompileParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:preCompileParser.ParameterTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#parameterList.
    def visitParameterList(self, ctx:preCompileParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:preCompileParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#statement.
    def visitStatement(self, ctx:preCompileParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#returnStatement.
    def visitReturnStatement(self, ctx:preCompileParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#expressionStatement.
    def visitExpressionStatement(self, ctx:preCompileParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#iterationStatement.
    def visitIterationStatement(self, ctx:preCompileParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#expression.
    def visitExpression(self, ctx:preCompileParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:preCompileParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#postfixExpression.
    def visitPostfixExpression(self, ctx:preCompileParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:preCompileParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:preCompileParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:preCompileParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#shiftExpression.
    def visitShiftExpression(self, ctx:preCompileParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#relationalExpression.
    def visitRelationalExpression(self, ctx:preCompileParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#equalityExpression.
    def visitEqualityExpression(self, ctx:preCompileParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#andExpression.
    def visitAndExpression(self, ctx:preCompileParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:preCompileParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:preCompileParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:preCompileParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:preCompileParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:preCompileParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:preCompileParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:preCompileParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by preCompileParser#mString.
    def visitMString(self, ctx:preCompileParser.MStringContext):
        return self.visitChildren(ctx)



del preCompileParser