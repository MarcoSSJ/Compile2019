# Generated from preCompile.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .preCompileParser import preCompileParser
else:
    from preCompileParser import preCompileParser

# This class defines a complete listener for a parse tree produced by preCompileParser.
class preCompileListener(ParseTreeListener):

    # Enter a parse tree produced by preCompileParser#program.
    def enterProgram(self, ctx:preCompileParser.ProgramContext):
        pass

    # Exit a parse tree produced by preCompileParser#program.
    def exitProgram(self, ctx:preCompileParser.ProgramContext):
        pass


    # Enter a parse tree produced by preCompileParser#include.
    def enterInclude(self, ctx:preCompileParser.IncludeContext):
        pass

    # Exit a parse tree produced by preCompileParser#include.
    def exitInclude(self, ctx:preCompileParser.IncludeContext):
        pass


    # Enter a parse tree produced by preCompileParser#define.
    def enterDefine(self, ctx:preCompileParser.DefineContext):
        pass

    # Exit a parse tree produced by preCompileParser#define.
    def exitDefine(self, ctx:preCompileParser.DefineContext):
        pass


    # Enter a parse tree produced by preCompileParser#translationUnit.
    def enterTranslationUnit(self, ctx:preCompileParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by preCompileParser#translationUnit.
    def exitTranslationUnit(self, ctx:preCompileParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by preCompileParser#function.
    def enterFunction(self, ctx:preCompileParser.FunctionContext):
        pass

    # Exit a parse tree produced by preCompileParser#function.
    def exitFunction(self, ctx:preCompileParser.FunctionContext):
        pass


    # Enter a parse tree produced by preCompileParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:preCompileParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by preCompileParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:preCompileParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by preCompileParser#compoundStatement.
    def enterCompoundStatement(self, ctx:preCompileParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by preCompileParser#compoundStatement.
    def exitCompoundStatement(self, ctx:preCompileParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by preCompileParser#compoundUnit.
    def enterCompoundUnit(self, ctx:preCompileParser.CompoundUnitContext):
        pass

    # Exit a parse tree produced by preCompileParser#compoundUnit.
    def exitCompoundUnit(self, ctx:preCompileParser.CompoundUnitContext):
        pass


    # Enter a parse tree produced by preCompileParser#declaration.
    def enterDeclaration(self, ctx:preCompileParser.DeclarationContext):
        pass

    # Exit a parse tree produced by preCompileParser#declaration.
    def exitDeclaration(self, ctx:preCompileParser.DeclarationContext):
        pass


    # Enter a parse tree produced by preCompileParser#initDeclaration.
    def enterInitDeclaration(self, ctx:preCompileParser.InitDeclarationContext):
        pass

    # Exit a parse tree produced by preCompileParser#initDeclaration.
    def exitInitDeclaration(self, ctx:preCompileParser.InitDeclarationContext):
        pass


    # Enter a parse tree produced by preCompileParser#initDeclarator.
    def enterInitDeclarator(self, ctx:preCompileParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by preCompileParser#initDeclarator.
    def exitInitDeclarator(self, ctx:preCompileParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by preCompileParser#initializer.
    def enterInitializer(self, ctx:preCompileParser.InitializerContext):
        pass

    # Exit a parse tree produced by preCompileParser#initializer.
    def exitInitializer(self, ctx:preCompileParser.InitializerContext):
        pass


    # Enter a parse tree produced by preCompileParser#declarator.
    def enterDeclarator(self, ctx:preCompileParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by preCompileParser#declarator.
    def exitDeclarator(self, ctx:preCompileParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by preCompileParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:preCompileParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by preCompileParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:preCompileParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by preCompileParser#parameterList.
    def enterParameterList(self, ctx:preCompileParser.ParameterListContext):
        pass

    # Exit a parse tree produced by preCompileParser#parameterList.
    def exitParameterList(self, ctx:preCompileParser.ParameterListContext):
        pass


    # Enter a parse tree produced by preCompileParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:preCompileParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by preCompileParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:preCompileParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by preCompileParser#statement.
    def enterStatement(self, ctx:preCompileParser.StatementContext):
        pass

    # Exit a parse tree produced by preCompileParser#statement.
    def exitStatement(self, ctx:preCompileParser.StatementContext):
        pass


    # Enter a parse tree produced by preCompileParser#returnStatement.
    def enterReturnStatement(self, ctx:preCompileParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by preCompileParser#returnStatement.
    def exitReturnStatement(self, ctx:preCompileParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by preCompileParser#expressionStatement.
    def enterExpressionStatement(self, ctx:preCompileParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by preCompileParser#expressionStatement.
    def exitExpressionStatement(self, ctx:preCompileParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by preCompileParser#iterationStatement.
    def enterIterationStatement(self, ctx:preCompileParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by preCompileParser#iterationStatement.
    def exitIterationStatement(self, ctx:preCompileParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by preCompileParser#expression.
    def enterExpression(self, ctx:preCompileParser.ExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#expression.
    def exitExpression(self, ctx:preCompileParser.ExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:preCompileParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:preCompileParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#postfixExpression.
    def enterPostfixExpression(self, ctx:preCompileParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#postfixExpression.
    def exitPostfixExpression(self, ctx:preCompileParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:preCompileParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by preCompileParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:preCompileParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by preCompileParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:preCompileParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:preCompileParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:preCompileParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:preCompileParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#shiftExpression.
    def enterShiftExpression(self, ctx:preCompileParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#shiftExpression.
    def exitShiftExpression(self, ctx:preCompileParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#relationalExpression.
    def enterRelationalExpression(self, ctx:preCompileParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#relationalExpression.
    def exitRelationalExpression(self, ctx:preCompileParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#equalityExpression.
    def enterEqualityExpression(self, ctx:preCompileParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#equalityExpression.
    def exitEqualityExpression(self, ctx:preCompileParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#andExpression.
    def enterAndExpression(self, ctx:preCompileParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#andExpression.
    def exitAndExpression(self, ctx:preCompileParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:preCompileParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:preCompileParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:preCompileParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:preCompileParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:preCompileParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:preCompileParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:preCompileParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:preCompileParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:preCompileParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:preCompileParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:preCompileParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by preCompileParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:preCompileParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by preCompileParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:preCompileParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by preCompileParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:preCompileParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by preCompileParser#mString.
    def enterMString(self, ctx:preCompileParser.MStringContext):
        pass

    # Exit a parse tree produced by preCompileParser#mString.
    def exitMString(self, ctx:preCompileParser.MStringContext):
        pass


