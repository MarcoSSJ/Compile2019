"""
预编译阶段,进行IDENTIFIER的值替换
"""
from antlr4 import *
from parser_.tinycLexer import tinycLexer
from parser_.tinycListener import tinycListener
from parser_.tinycParser import tinycParser
from parser_.tinycVisitor import  tinycVisitor
from util import *
from MacroTable import MacroTable,MacroList
# This class defines a complete generic visitor for a parse tree produced by tinycParser.


class preCompiler(tinycVisitor):

    def __init__(self, output:str, table:MacroTable):
        super(preCompiler, self).__init__()
        self.module = ir.Module()
        self.table = table
        self.f = open(output, 'w')
        self.define = []
        self.find_params = False ##using when find a macro func
        pass

    def StringCtx(self, ctx):
        """通用的返回string方法,当子节点为lexer节点时,加上getTExt(),否则加上返回值,空格为了防止c程序inti这种情况错误"""
        s = ''
        for child in ctx.children:
            text = self.visit(child)
            if text:
                s += text + ' '
            else:
                s += child.getText() + ' '
        return s

    # Visit a parse tree produced by tinycParser#program.
    def visitProgram(self, ctx:tinycParser.ProgramContext):
        s = ''
        if ctx.EOF():#EOF会生成<EOF>从而报错
            children = ctx.children[:-1]
        else:
            children = ctx.children
        for child in children:
            text = self.visit(child)
            if text:
                s += text + ' '
            else:
                s += child.getText() + ' '
        print(s)
        self.f.write(s)

    # Visit a parse tree produced by tinycParser#include.
    def visitInclude(self, ctx:tinycParser.IncludeContext):
        pass

    def visitDefine(self, ctx:tinycParser.DefineContext):
        pass

    # Visit a parse tree produced by tinycParser#translationUnit.
    def visitTranslationUnit(self, ctx:tinycParser.TranslationUnitContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#function.
    def visitFunction(self, ctx:tinycParser.FunctionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:tinycParser.TypeSpecifierContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#compoundStatement.
    def visitCompoundStatement(self, ctx:tinycParser.CompoundStatementContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#compoundUnit.
    def visitCompoundUnit(self, ctx:tinycParser.CompoundUnitContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#declaration.
    def visitDeclaration(self, ctx:tinycParser.DeclarationContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#initDeclaration.
    def visitInitDeclaration(self, ctx:tinycParser.InitDeclarationContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#initDeclarator.
    def visitInitDeclarator(self, ctx:tinycParser.InitDeclaratorContext):
        return self.StringCtx(ctx)

    # Visit a parse tree produced by tinycParser#initializer.
    def visitInitializer(self, ctx:tinycParser.InitializerContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#declarator.
    def visitDeclarator(self, ctx:tinycParser.DeclaratorContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#directDeclarator.
    def visitDirectDeclarator(self, ctx:tinycParser.DirectDeclaratorContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#constantExpression.
    def visitConstantExpression(self, ctx:tinycParser.ConstantExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:tinycParser.ParameterTypeListContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#parameterList.
    def visitParameterList(self, ctx:tinycParser.ParameterListContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:tinycParser.ParameterDeclarationContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#statement.
    def visitStatement(self, ctx:tinycParser.StatementContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#returnStatement.
    def visitJumpStatement(self, ctx:tinycParser.JumpStatementContext):
        return self.StringCtx(ctx)

    # Visit a parse tree produced by tinycParser#expressionStatement.
    def visitExpressionStatement(self, ctx:tinycParser.ExpressionStatementContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#selectionStatement.
    def visitSelectionStatement(self, ctx:tinycParser.SelectionStatementContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#iterationStatement.
    def visitIterationStatement(self, ctx:tinycParser.IterationStatementContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#expression.
    def visitExpression(self, ctx:tinycParser.ExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:tinycParser.AssignmentExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#postfixExpression.
    def visitPostfixExpression(self, ctx:tinycParser.PostfixExpressionContext):
        """postfix会识别关键字,所以需要特殊处理"""
        if len(ctx.children) == 1:
            text = ctx.primaryExpression().getText()
            mlist = self.table.table.get(text)
            if mlist and not len(mlist.params):
                s = ''.join(mlist.tokens)
                return s
            else:
                return self.StringCtx(ctx)

        elif ctx.children[1].getText() == '(':
            """此时假设遇到了macro函数,进行处理"""
            text = ctx.postfixExpression().getText()
            print("the macro func can be ", text)
            mlist = self.table.table.get(text)
            if mlist and len(ctx.children) == 4:
                self.find_params = True
                arglist = self.visit(ctx.argumentExpressionList())
                mlist = self.table.table.get(text)
                s = mlist.complicateTokenStream(arglist)
                self.find_params = False
                return s
            else:
                return self.StringCtx(ctx)
        else:
            return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:tinycParser.ArgumentExpressionListContext):
        if self.find_params:
            if len(ctx.children) == 1:
                arg_list = []
            else:
                arg_list = self.visit(ctx.argumentExpressionList())
            arg = self.visit(ctx.assignmentExpression())
            print('arg is ', arg)
            arg_list.append(arg)
            return arg_list
        else:
            return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#unaryExpression.
    def visitUnaryExpression(self, ctx:tinycParser.UnaryExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:tinycParser.MultiplicativeExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:tinycParser.AdditiveExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#shiftExpression.
    def visitShiftExpression(self, ctx:tinycParser.ShiftExpressionContext):
        return self.StringCtx(ctx)

    # Visit a parse tree produced by tinycParser#relationalExpression.
    def visitRelationalExpression(self, ctx:tinycParser.RelationalExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#equalityExpression.
    def visitEqualityExpression(self, ctx:tinycParser.EqualityExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#andExpression.
    def visitAndExpression(self, ctx:tinycParser.AndExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:tinycParser.ExclusiveOrExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:tinycParser.InclusiveOrExpressionContext):
        return self.StringCtx(ctx)

    # Visit a parse tree produced by tinycParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:tinycParser.LogicalAndExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:tinycParser.LogicalOrExpressionContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:tinycParser.ConditionalExpressionContext):
        return self.StringCtx(ctx)

    # Visit a parse tree produced by tinycParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:tinycParser.AssignmentOperatorContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#unaryOperator.
    def visitUnaryOperator(self, ctx:tinycParser.UnaryOperatorContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:tinycParser.PrimaryExpressionContext):
        return self.StringCtx(ctx)

    # Visit a parse tree produced by tinycParser#mString.
    def visitMString(self, ctx:tinycParser.MStringContext):
        return self.StringCtx(ctx)

    def visitInitializerList(self, ctx:tinycParser.InitializerListContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#designation.
    def visitDesignation(self, ctx:tinycParser.DesignationContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#designatorList.
    def visitDesignatorList(self, ctx:tinycParser.DesignatorListContext):
        return self.StringCtx(ctx)


    # Visit a parse tree produced by tinycParser#designator.
    def visitDesignator(self, ctx:tinycParser.DesignatorContext):
        return self.StringCtx(ctx)
