# Generated from tinyc.g4 by ANTLR 4.7.2
from antlr4 import *
from parser_.tinycLexer import tinycLexer
from parser_.tinycListener import tinycListener
from parser_.tinycParser import tinycParser
from parser_.tinycVisitor import  tinycVisitor
from llvmlite import ir
from util import *
from SymbolTable import SymbolTable
# This class defines a complete generic visitor for a parse tree produced by tinycParser.

class c2llvmVisitor(tinycVisitor):

    def __init__(self):
        super(c2llvmVisitor, self).__init__()
        self.module = ir.Module()
        self.scope_depth = 0
        self.module.triple = "x86_64-unknown-linux-gnu" # llvm.Target.from_default_triple()
        self.module.data_layout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

        # 符号表
        self.symbol_table = {}
        printf_type = ir.FunctionType(LLVMTypes().int32, [ir.PointerType(LLVMTypes().int8)], var_arg=True)
        printf_func = ir.Function(self.module, printf_type, "printf")
        self.symbol_table['printf'] = printf_func
        self.cur_type = None
        self.constants = 0
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
        print('visit include', ctx.getChild(2).getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#translationUnit.
    def visitTranslationUnit(self, ctx:tinycParser.TranslationUnitContext):
        print('visit trans unit')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#function.
    def visitFunction(self, ctx:tinycParser.FunctionContext):
        self.scope_depth += 1
        ret_type = self.visit(ctx.getChild(0))
        self.cur_type = ret_type
        _, func_name, func_type, arg_names = self.visit(ctx.getChild(1))


        llvm_func = ir.Function(self.module, func_type, name=func_name)
        self.builder = ir.IRBuilder(llvm_func.append_basic_block(name=".entry"))
        for arg, llvm_arg in zip(arg_names, llvm_func.args):
            self.symbol_table[arg] = llvm_arg

        self.visit(ctx.compoundStatement())
        return


    # Visit a parse tree produced by tinycParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:tinycParser.TypeSpecifierContext):
        text = ctx.getText()
        if text == 'int':
            return ir.IntType(32)
        elif text == 'void':
            return ir.VoidType()
        elif text == 'char':
            return ir.IntType(8)
        else:
            ##TODO error
            pass


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

    # Visit a parse tree produced by tinycParser#returnStatement.
    def visitReturnStatement(self, ctx:tinycParser.ReturnStatementContext):
        jump_instru = ctx.children[0].getText()
        if jump_instru == 'return':
            if len(ctx.children) == 2:
                self.builder.ret_void()
            else:
                ret_val = self.visit(ctx.expression())
                # TODO: cast type
                self.builder.ret(ret_val)

    # Visit a parse tree produced by tinycParser#expressionStatement.
    def visitExpressionStatement(self, ctx:tinycParser.ExpressionStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by tinycParser#declarator.
    def visitDeclarator(self, ctx:tinycParser.DeclaratorContext):
        """返回_, func_name, func_type, arg_names"""
        if len(ctx.children) == 1:
            # :   IDENTIFIER
            # TODO: 检查这里返回值
            return None ,ctx.IDENTIFIER().getText(), self.cur_type, []
        else:
            func_name = ctx.IDENTIFIER().getText()
            if len(ctx.children) == 4:
                (arg_names, arg_types), var_arg = self.visit(ctx.parameterTypeList())
                new_llvm_type = ir.FunctionType(self.cur_type, arg_types, var_arg=var_arg)
                # 代表有参数列表
                return None, func_name,new_llvm_type, arg_names
            else:
                arg_names = []
                arg_types = []
                new_llvm_type = ir.FunctionType(self.cur_type, arg_types)
                return None,  func_name, new_llvm_type, arg_names

    # Visit a parse tree produced by tinycParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:tinycParser.ParameterTypeListContext):
        if len(ctx.children) == 3:
            return self.visit(ctx.parameterList()), True
        else:
            return self.visit(ctx.parameterList()), False


    # Visit a parse tree produced by tinycParser#parameterList.
    def visitParameterList(self, ctx:tinycParser.ParameterListContext):
        ### C是从右向左压参的
        cnt = ctx.getChildCount()
        names, types = [], []
        for index in range(0, cnt, 2):
            bn, bt = self.visit(ctx.getChild(index))
            names.append(bn)
            types.append(bt)
        return names, types

    # Visit a parse tree produced by tinycParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:tinycParser.ParameterDeclarationContext):
        # TODO:现在parameter生成不太对
        self.cur_type = self.visit(ctx.typeSpecifier())
        _, argname, argtype, _ = self.visit(ctx.declarator())
        return argname, argtype


    # Visit a parse tree produced by tinycParser#statement.
    def visitStatement(self, ctx:tinycParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#expression.
    def visitExpression(self, ctx:tinycParser.ExpressionContext):
        cnt = ctx.getChildCount()
        val = self.visit(ctx.getChild(0))
        for index in range(2, cnt, 2):
            val = self.visit(ctx.getChild(index))
        return val


    # Visit a parse tree produced by tinycParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:tinycParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)

    def visitArgumentExpressionList(self, ctx:tinycParser.ArgumentExpressionListContext):
        if len(ctx.children) == 1:
            arg_list = []
        else:
            arg_list = self.visit(ctx.argumentExpressionList())
        arg = self.visit(ctx.assignmentExpression())
        arg_list.append(arg)
        return arg_list


    # Visit a parse tree produced by tinycParser#postfixExpression.
    def visitPostfixExpression(self, ctx:tinycParser.PostfixExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.primaryExpression())
        else:
            left_exp = self.visit(ctx.postfixExpression())
            op = ctx.children[1].getText()
            if op == '(':
                args = []
                if len(ctx.children) == 4:
                    args = self.visit(ctx.argumentExpressionList())
                #TODO 类型转换
                print('left' , left_exp)
                print('args' , args)
                return self.builder.call(left_exp, args)



    # Visit a parse tree produced by tinycParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:tinycParser.PrimaryExpressionContext):
        text = ctx.getText()
        if ctx.IDENTIFIER():
            if text in self.symbol_table:
                var = self.symbol_table[text]
                if type(var) is ir.Function: #函数名直接返回
                    return var
        elif ctx.STRING():
            idx = self.constants
            self.constants += 1
            text = text[1:-1]
            strlen = len(text) + 1
            print(f'strlen {strlen}')
            string = get_const_from_str('string', text)
            print(string)
            const = ir.GlobalVariable(self.module, ir.ArrayType(LLVMTypes.int8,strlen), ".str%d"%idx)
            const.global_constant = True
            const.initializer = string
            zero = ir.Constant(LLVMTypes.int32, 0)
            arg = self.builder.gep(const, [zero,zero], inbounds=True)
            return arg
        elif ctx.CONSTANT():
            return get_const_from_str('int', text)

