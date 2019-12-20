# Generated from tinyc.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tinycParser import tinycParser
else:
    from tinycParser import tinycParser

# This class defines a complete generic visitor for a parse tree produced by tinycParser.

class tinycVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tinycParser#program.
    def visitProgram(self, ctx:tinycParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#include.
    def visitInclude(self, ctx:tinycParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#translationUnit.
    def visitTranslationUnit(self, ctx:tinycParser.TranslationUnitContext):
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


    # Visit a parse tree produced by tinycParser#returnStatement.
    def visitReturnStatement(self, ctx:tinycParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#expressionStatement.
    def visitExpressionStatement(self, ctx:tinycParser.ExpressionStatementContext):
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


    # Visit a parse tree produced by tinycParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:tinycParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:tinycParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:tinycParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#shiftExpression.
    def visitShiftExpression(self, ctx:tinycParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#relationalExpression.
    def visitRelationalExpression(self, ctx:tinycParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#equalityExpression.
    def visitEqualityExpression(self, ctx:tinycParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#andExpression.
    def visitAndExpression(self, ctx:tinycParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:tinycParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:tinycParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:tinycParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:tinycParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:tinycParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:tinycParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:tinycParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)



del tinycParser