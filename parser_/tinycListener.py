# Generated from tinyc.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tinycParser import tinycParser
else:
    from tinycParser import tinycParser

# This class defines a complete listener for a parse tree produced by tinycParser.
class tinycListener(ParseTreeListener):

    # Enter a parse tree produced by tinycParser#program.
    def enterProgram(self, ctx:tinycParser.ProgramContext):
        pass

    # Exit a parse tree produced by tinycParser#program.
    def exitProgram(self, ctx:tinycParser.ProgramContext):
        pass


    # Enter a parse tree produced by tinycParser#include.
    def enterInclude(self, ctx:tinycParser.IncludeContext):
        pass

    # Exit a parse tree produced by tinycParser#include.
    def exitInclude(self, ctx:tinycParser.IncludeContext):
        pass


    # Enter a parse tree produced by tinycParser#translationUnit.
    def enterTranslationUnit(self, ctx:tinycParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by tinycParser#translationUnit.
    def exitTranslationUnit(self, ctx:tinycParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by tinycParser#function.
    def enterFunction(self, ctx:tinycParser.FunctionContext):
        pass

    # Exit a parse tree produced by tinycParser#function.
    def exitFunction(self, ctx:tinycParser.FunctionContext):
        pass


    # Enter a parse tree produced by tinycParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:tinycParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by tinycParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:tinycParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by tinycParser#compoundStatement.
    def enterCompoundStatement(self, ctx:tinycParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by tinycParser#compoundStatement.
    def exitCompoundStatement(self, ctx:tinycParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by tinycParser#compoundUnit.
    def enterCompoundUnit(self, ctx:tinycParser.CompoundUnitContext):
        pass

    # Exit a parse tree produced by tinycParser#compoundUnit.
    def exitCompoundUnit(self, ctx:tinycParser.CompoundUnitContext):
        pass


    # Enter a parse tree produced by tinycParser#declaration.
    def enterDeclaration(self, ctx:tinycParser.DeclarationContext):
        pass

    # Exit a parse tree produced by tinycParser#declaration.
    def exitDeclaration(self, ctx:tinycParser.DeclarationContext):
        pass


    # Enter a parse tree produced by tinycParser#initDeclaration.
    def enterInitDeclaration(self, ctx:tinycParser.InitDeclarationContext):
        pass

    # Exit a parse tree produced by tinycParser#initDeclaration.
    def exitInitDeclaration(self, ctx:tinycParser.InitDeclarationContext):
        pass


    # Enter a parse tree produced by tinycParser#initDeclarator.
    def enterInitDeclarator(self, ctx:tinycParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by tinycParser#initDeclarator.
    def exitInitDeclarator(self, ctx:tinycParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by tinycParser#declarator.
    def enterDeclarator(self, ctx:tinycParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by tinycParser#declarator.
    def exitDeclarator(self, ctx:tinycParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by tinycParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:tinycParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by tinycParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:tinycParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by tinycParser#parameterList.
    def enterParameterList(self, ctx:tinycParser.ParameterListContext):
        pass

    # Exit a parse tree produced by tinycParser#parameterList.
    def exitParameterList(self, ctx:tinycParser.ParameterListContext):
        pass


    # Enter a parse tree produced by tinycParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:tinycParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by tinycParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:tinycParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by tinycParser#statement.
    def enterStatement(self, ctx:tinycParser.StatementContext):
        pass

    # Exit a parse tree produced by tinycParser#statement.
    def exitStatement(self, ctx:tinycParser.StatementContext):
        pass


    # Enter a parse tree produced by tinycParser#returnStatement.
    def enterReturnStatement(self, ctx:tinycParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by tinycParser#returnStatement.
    def exitReturnStatement(self, ctx:tinycParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by tinycParser#expressionStatement.
    def enterExpressionStatement(self, ctx:tinycParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by tinycParser#expressionStatement.
    def exitExpressionStatement(self, ctx:tinycParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by tinycParser#expression.
    def enterExpression(self, ctx:tinycParser.ExpressionContext):
        pass

    # Exit a parse tree produced by tinycParser#expression.
    def exitExpression(self, ctx:tinycParser.ExpressionContext):
        pass


    # Enter a parse tree produced by tinycParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:tinycParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by tinycParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:tinycParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by tinycParser#postfixExpression.
    def enterPostfixExpression(self, ctx:tinycParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by tinycParser#postfixExpression.
    def exitPostfixExpression(self, ctx:tinycParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by tinycParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:tinycParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by tinycParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:tinycParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by tinycParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:tinycParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by tinycParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:tinycParser.PrimaryExpressionContext):
        pass


