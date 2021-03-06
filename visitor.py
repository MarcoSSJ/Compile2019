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

    BASE = 0
    ARRAY = 1
    FUNC = 2

    def __init__(self):
        super(c2llvmVisitor, self).__init__()
        self.module = ir.Module()
        self.scope_depth = 0
        self.module.triple = "x86_64-unknown-linux-gnu" # llvm.Target.from_default_triple()
        self.module.data_layout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

        # 符号表
        self.symbol_table = SymbolTable()
        printf_type = ir.FunctionType(LLVMTypes().int32, [ir.PointerType(LLVMTypes().int8)], var_arg=True)
        printf_func = ir.Function(self.module, printf_type, "printf")
        self.symbol_table.addSymbol('printf' , printf_func)
        self.cur_type = None
        self.constants = 0
        self.continue_block, self.break_block = None, None
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
        self.symbol_table.enterScope()
        ret_type = self.visit(ctx.getChild(0))
        self.cur_type = ret_type
        _, func_name, func_type, arg_names = self.visit(ctx.getChild(1))

        val = self.symbol_table.getSymbol(func_name)
        if val:
            # TODO 错误处理
            raise Exception("redefine function error!")
        else:
            llvm_func = ir.Function(self.module, func_type, name=func_name)
            print("func is", func_name, func_type)
            self.symbol_table.addSymbol(func_name, llvm_func)
            self.builder = ir.IRBuilder(llvm_func.append_basic_block(name=".entry"+func_name))
        self.symbol_table.enterScope()
        for arg, llvm_arg in zip(arg_names, llvm_func.args):
            print('func add argname', arg, llvm_arg)
            print(type(llvm_arg))
            self.symbol_table.addSymbol(arg, llvm_arg)
        self.continue_block = None
        self.break_block = None
        self.visit(ctx.compoundStatement())
        self.symbol_table.exitScope()
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
        var_type = self.visit(ctx.typeSpecifier())
        self.cur_type = var_type
        print('var_type:', var_type)
        init_list = self.visit(ctx.initDeclaration())

    # Visit a parse tree produced by tinycParser#initDeclaration.
    def visitInitDeclaration(self, ctx:tinycParser.InitDeclarationContext):
        cnt = ctx.getChildCount()
        declarator = None
        for index in range(0, cnt, 2):
            declarator = self.visit(ctx.getChild(index))
        return declarator

    # Visit a parse tree produced by tinycParser#initDeclarator.
    def visitInitDeclarator(self, ctx:tinycParser.InitDeclaratorContext):
        tpe, name, llvm_tpe, size = self.visit(ctx.declarator())
        has_init = (len(ctx.children) == 3)
        if tpe == self.BASE:
            # 分配内存
            addr = self.builder.alloca(llvm_tpe)
            try:
                self.symbol_table.addSymbol(name, addr)
                if has_init:
                    init_val = self.visit(ctx.initializer())
                    # if type(init_val) != ir.Constant: #TODO:check here我觉得问题很大
                    #     converted_val = ir.Constant(llvm_tpe,init_val)
                    # else:
                    converted_val = init_val
                    print('initiaze to ', init_val)
                    print(isinstance(init_val, ir.IntType))
                    print(type(init_val))
                    print('help me teacher!!',init_val, addr)
                    self.builder.store(converted_val, addr)
            except Exception as e:
                raise e

        elif tpe == self.FUNC :
            raise Exception("init declarator cannot be a func")
            #TODO: error
        elif tpe == self.ARRAY:
            var_type = llvm_tpe

            try:

                print('var_name type', name, var_type)
                if has_init:
                    init_val = self.visit(ctx.initializer())
                    if isinstance(init_val, list):
                        converted_val = ir.Constant(var_type, init_val)
                    else:
                        var_type = init_val.type
                        converted_val = init_val
                        print('Array initiaze to ', init_val, type(init_val))
                addr = self.builder.alloca(var_type)
                print('addr', addr, 'llvm_tpe', llvm_tpe)
                self.symbol_table.addSymbol(name, addr)
                if has_init:
                    self.builder.store(converted_val, addr)
                    #print('self.builder.module', self.builder.block.instructions)
            except Exception as e:
                raise e

    def visitInitializer(self, ctx:tinycParser.InitializerContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.assignmentExpression())
        else:
            return self.visit(ctx.initializerList())

    def visitInitializerList(self, ctx:tinycParser.InitializerListContext):
        print('visitInitializerList', ctx.children)
        init_list = []
        if len(ctx.children) != 1:
            init_list = self.visit(ctx.initializerList())
        init_list.append(self.visit(ctx.initializer()))
        print('init_list', init_list)
        return init_list

    def visitIterationStatement(self, ctx:tinycParser.IterationStatementContext):
        self.symbol_table.enterScope()
        prefix = self.builder.block.name

        keyword = ctx.getChild(0).getText()
        if keyword == 'for':
            #初始化语句
            child_idx = 2
            if getRuleName(ctx.children[child_idx]) == 'expression':
                self.visit(ctx.children[child_idx])
                child_idx += 2
            elif getRuleName(ctx.children[child_idx]) == 'declaration':
                self.visit(ctx.declaration())
                child_idx += 1
            else:
                child_idx += 1

            start_block = self.builder.append_basic_block(name=prefix+".loop_start")
            cond_block = self.builder.append_basic_block(name=prefix+".loop_cond")
            loop_block = self.builder.append_basic_block(name=prefix+".loop_body")
            update_block = self.builder.append_basic_block(name=prefix+".loop_update")
            end_block = self.builder.append_basic_block(name=prefix+".loop_end")


            last_continue, last_break = self.continue_block, self.break_block
            self.continue_block, self.break_block = update_block, end_block

            self.builder.branch(start_block)
            self.builder.position_at_start(start_block)

            self.builder.branch(cond_block)
            self.builder.position_at_start(cond_block)

            if getRuleName(ctx.children[child_idx]) == 'expression':
                cond_val = self.visit(ctx.children[child_idx])
                print('cond_val',cond_val.flags)
                cond_val = whether_is_true(self.builder, cond_val)
                buf = cond_val.get_reference()

                buf = LLVMTypes.bool(buf)
                print('converted_cond', buf)

                self.builder.cbranch(buf, loop_block, end_block)
                child_idx += 2
            else:
                child_idx += 1
                self.builder.branch(loop_block)

            self.builder.position_at_start(loop_block)
            self.visit(ctx.statement())
            self.builder.branch(update_block)

            self.builder.position_at_start(update_block)
            if getRuleName(ctx.children[child_idx]) == 'expression':
                self.visit(ctx.children[child_idx])
                child_idx += 2
            else:
                child_idx += 1
            self.builder.branch(cond_block)

            self.builder.position_at_start(end_block)
            self.symbol_table.exitScope()
            self.continue_block = last_continue
            self.break_block = last_break
            #TODO: continue break[-=/        return self.visitChildren(ctx)

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
        elif jump_instru == 'continue':
             if self.continue_block is None:
                raise Exception("continue can not be used here", ctx)
             self.builder.branch(self.continue_block)
        else:
            raise Exception('not implemented')

    # Visit a parse tree produced by tinycParser#expressionStatement.
    def visitExpressionStatement(self, ctx:tinycParser.ExpressionStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by tinycParser#declarator.
    def visitDeclarator(self, ctx:tinycParser.DeclaratorContext):
        """返回_, func_name, func_type, arg_names"""
        print('visitDeclarator:', ctx.children, ctx.getText())
        tpe, name, llvm_type, arg = self.visit(ctx.directDeclarator())
        print('after decl: tpe name ', tpe, name, llvm_type, arg)
        if tpe == self.ARRAY:
            if arg:
                for size in reversed(arg):
                    print('before llvm_type:', llvm_type, arg)
                    llvm_type = ir.ArrayType(element=llvm_type, count=size)
                    print('llvm_type:', llvm_type, arg)
                    return tpe, name, llvm_type, []
            return tpe, name, llvm_type, []
        else:
            return tpe, name, llvm_type, arg



    def visitDirectDeclarator(self, ctx:tinycParser.DirectDeclaratorContext):
        print('visitDirectDeclarator', ctx.getText())
        if len(ctx.children) == 1:
            # :   IDENTIFIER
            # TODO: 检查这里返回值
            # print('Base:', self.cur_type)
            return self.BASE ,ctx.IDENTIFIER().getText(), self.cur_type, []
        else:
            op = ctx.children[1].getText()
            # 函数
            old_type = self.cur_type
            if op == '(':
                func_name = ctx.children[0].getText()
                if len(ctx.children) == 4:
                    (arg_names, arg_types), var_arg = self.visit(ctx.parameterTypeList())
                    new_llvm_type = ir.FunctionType(old_type, arg_types, var_arg=var_arg)
                    # 代表有参数列表
                    return self.FUNC, func_name,new_llvm_type, arg_names
                else:
                    arg_names = []
                    arg_types = []
                    new_llvm_type = ir.FunctionType(old_type, arg_types)
                    return self.FUNC, func_name, new_llvm_type, arg_names
            elif op == '[':
                tpe, arrayname, old_type, array_nums = self.visit(ctx.directDeclarator())
                print('arrayname', arrayname, ctx.children, len(ctx.children), tpe, old_type, array_nums)
                if len(ctx.children) >= 4:
                    try:
                        array_size= int(ctx.constantExpression().getText())
                        array_nums.append(array_size)
                        # llvm_type = ir.PointerType(old_type)
                        print('return ARRAY', self.ARRAY, arrayname, old_type, array_nums)
                        return self.ARRAY, arrayname, old_type, array_nums
                    except:
                        raise Exception('only constant value are supported')
                else:
                    arrayname = ctx.children[0].getText()
                    print("current type", old_type)
                    llvm_type = ir.PointerType(old_type)
                    print("param type", llvm_type)
                    return self.ARRAY, arrayname, llvm_type, None
                    # return self.ARRAY, arrayname, ,None


    # Visit a parse tree produced by tinycParser#constantExpression.
    def visitConstantExpression(self, ctx:tinycParser.ConstantExpressionContext):
        var, addr = self.visit(ctx.conditionalExpression())
        return var

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

    def visitExpression(self, ctx:tinycParser.ExpressionContext):
        cnt = ctx.getChildCount()
        val = self.visit(ctx.getChild(0))
        for index in range(2, cnt, 2):
            val = self.visit(ctx.getChild(index))
        return val

    # Visit a parse tree produced by tinycParser#selectionStatement.
    def visitSelectionStatement(self, ctx: tinycParser.SelectionStatementContext):
        if ctx.children[0].getText() == 'if':
            value = self.visit(ctx.children[2])
            value = whether_is_true(self.builder, value)
            value = value.get_reference()
            condition = ir.IntType(1)(value)
            self.symbol_table.enterScope()
            if len(ctx.children) > 5:
                with self.builder.if_else(condition) as (then, otherwise):
                    with then:
                        self.visit(ctx.children[4])
                    with otherwise:
                        self.visit(ctx.children[6])
            else:
                with self.builder.if_then(condition):
                    self.visit(ctx.children[4])
            self.symbol_table.exitScope()

    # Visit a parse tree produced by tinycParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:tinycParser.AssignmentExpressionContext):
        if(len(ctx.children)) == 3:
            var, addr = self.visit(ctx.unaryExpression())
            op = ctx.getChild(1).getText()
            val = self.visit(ctx.assignmentExpression())
            if op == "=":
                self.builder.store(val, addr)
                print('val, addr', val, '\n', addr)
                return val
            elif op == "+=":
                add = self.builder.add(var, val)
                print('add, addr, var', add,'\n', addr,'\n', var)
                self.builder.store(add, addr)
                return var #TODO:check here
            elif op == "-=":
                sub = self.builder.sub(var, val)
                self.builder.store(sub, addr)
                return var
            elif op == "*=":
                mul = self.builder.mul(var, val)
                self.builder.store(mul, addr)
                return var
            elif op == "/=":
                mul = self.builder.sdiv(var, val)
                self.builder.store(mul, addr)
                return var
            elif op == "%=":
                rem = self.builder.srem(var, val)
                self.builder.store(rem, addr)
                return var
            else:
                raise  Exception('not implemented')
        else:
            val, addr = self.visit(ctx.conditionalExpression())
            return val


    def visitArgumentExpressionList(self, ctx:tinycParser.ArgumentExpressionListContext):
        if len(ctx.children) == 1:
            arg_list = []
        else:
            arg_list = self.visit(ctx.argumentExpressionList())
        arg = self.visit(ctx.assignmentExpression())
        print('arg is ', arg)
        arg_list.append(arg)
        return arg_list


    # Visit a parse tree produced by tinycParser#postfixExpression.
    def visitPostfixExpression(self, ctx:tinycParser.PostfixExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.primaryExpression())
        else:
            left_exp, addr = self.visit(ctx.postfixExpression())
            op = ctx.children[1].getText()
            if op == '(':
                args = []
                if len(ctx.children) == 4:
                    args = self.visit(ctx.argumentExpressionList())
                converted_args = []
                # TODO 类型转换
                for arg, param in zip(args, left_exp.args):
                    if (type(arg.type) is ir.ArrayType) and \
                            (type(param.type) is ir.PointerType):
                        arg = arr_to_llvm_pointer(self.builder, arg)
                        converted_args.append(arg)
                    else:
                        converted_args.append(arg)
                if len(converted_args) < len(args):  # 考虑变长参数
                    converted_args += args[len(left_exp.args):]
                return self.builder.call(left_exp, converted_args), None
            elif op == '[':

                idx = self.visit(ctx.expression())
                # if type(left_exp.type) in [ir.ArrayType]:
                #     var = self.builder.extract_value(left_exp, val.constant)
                #     return var, None
                zero = ir.Constant(LLVMTypes.int, 0)
                if type(left_exp) is ir.Argument:
                    array_indices = [idx]
                else:
                    array_indices = [zero, idx]
                print("postif []the val is ",idx, "left " , addr)
                addr = self.builder.gep(addr, array_indices)
                # tmp = self.builder.alloca(val.type)
                # self.builder.store(val, tmp)
                # addr = self.builder.gep(tmp, [val])
                print("addr is ",addr)

                var = self.builder.load(addr)
                return var, addr
            elif op == '++':
                one = left_exp.type(1)
                print('one', one)
                res = self.builder.add(left_exp, one)
                print('++', addr, res)
                if addr:
                    val = self.builder.store(res, addr)
                print('++', addr)
                return left_exp, addr
            elif op == '--':
                one = left_exp.type(1)
                print('one', one)
                res = self.builder.sub(left_exp, one)
                if addr: #++可以放在右值后
                    val = self.builder.store(res, addr)
                return left_exp, addr

    def visitUnaryExpression(self, ctx:tinycParser.UnaryExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.children[0])
        else:
            text = ctx.children[0].getText()
            val, addr = self.visit(ctx.unaryExpression())
            if text == '++':
                one = val.type(1)
                res = self.builder.add(val, one)
                self.builder.store(res, addr)
                return res, addr
            elif text == '--':
                one = val.type(1)
                res = self.builder.sub(val, one)
                self.builder.store(res, addr)
                return res, addr
            elif text == '+':
                return val, None
            elif text == '-':
                neg = self.builder.neg(val)
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!neg is ', neg)
                return neg, None

    # Visit a parse tree produced by tinycParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx: tinycParser.MultiplicativeExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.children[0])
        else:
            lhs, laddr = self.visit(ctx.children[0])
            rhs, raddr = self.visit(ctx.children[2])
            op = ctx.children[1].getText()
            if op == '*':
                return self.builder.mul(lhs, rhs), None
            elif op == '/':
                return self.builder.sdiv(lhs, rhs), None
            else:
                return self.builder.srem(lhs, rhs), None

    # Visit a parse tree produced by tinycParser#additiveExpression.
    def visitAdditiveExpression(self, ctx: tinycParser.AdditiveExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.multiplicativeExpression())
        else:
            lhs, laddr = self.visit(ctx.children[0])
            rhs, raddr  = self.visit(ctx.children[2])
            op = ctx.children[1].getText()
            if op == '+':
                return self.builder.add(lhs, rhs), None
            else:
                return self.builder.sub(lhs, rhs), None

    # Visit a parse tree produced by tinycParser#shiftExpression.
    def visitShiftExpression(self, ctx: tinycParser.ShiftExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.additiveExpression())
        else:
            lhs, laddr = self.visit(ctx.children[0])
            rhs, raddr = self.visit(ctx.children[2])
            op = ctx.children[1].getText()
            if op == '<<':
                return self.builder.shl(lhs, rhs), None
            else:
                return self.builder.ashr(lhs, rhs), None

    # Visit a parse tree produced by tinycParser#relationalExpression.
    def visitRelationalExpression(self, ctx: tinycParser.RelationalExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.shiftExpression())
        else:
            lhs, laddr = self.visit(ctx.children[0])
            rhs, raddr = self.visit(ctx.children[2])
            op = ctx.children[1].getText()
            build = self.builder.icmp_signed(cmpop=op, lhs=lhs, rhs=rhs)
            print('relation build', build, lhs, rhs)

            return build, None

    # Visit a parse tree produced by tinycParser#equalityExpression.
    def visitEqualityExpression(self, ctx: tinycParser.EqualityExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.relationalExpression())
        else:
            lhs, laddr = self.visit(ctx.children[0])
            rhs, raddr = self.visit(ctx.children[2])
            op = ctx.children[1].getText()
            return self.builder.icmp_signed(cmpop=op, lhs=lhs, rhs=rhs), None

    # Visit a parse tree produced by tinycParser#andExpression.
    def visitAndExpression(self, ctx: tinycParser.AndExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.equalityExpression())
        else:
            lhs, laddr = self.visit(ctx.children[0])
            rhs, raddr = self.visit(ctx.children[2])
            op = ctx.children[1].getText()
            return self.builder.and_(lhs, rhs), None

    # Visit a parse tree produced by tinycParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx: tinycParser.ExclusiveOrExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.andExpression())
        else:
            lhs, laddr = self.visit(ctx.children[0])
            rhs, raddr = self.visit(ctx.children[2])
            op = ctx.children[1].getText()
            return self.builder.xor(lhs, rhs), None

    # Visit a parse tree produced by tinycParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx: tinycParser.InclusiveOrExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.exclusiveOrExpression())
        else:
            lhs, laddr = self.visit(ctx.children[0])
            rhs, raddr = self.visit(ctx.children[2])
            op = ctx.children[1].getText()
            return self.builder.or_(lhs, rhs), None

    # Visit a parse tree produced by tinycParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx: tinycParser.LogicalAndExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.inclusiveOrExpression())
        else:
            lhs = (self.visit(ctx.children[0])[0])
            result = self.builder.alloca(ir.IntType(1))
            converted = whether_is_true(self.builder, lhs)
            cond = LLVMTypes.bool(converted.get_reference())
            with self.builder.if_else(cond) as (then, otherwise):
                with then:
                    rhs, rhs_ptr = self.visit(ctx.inclusiveOrExpression())
                    converted_rhs = whether_is_true(self.builder,rhs )
                    self.builder.store(converted_rhs, result)
                with otherwise:
                    self.builder.store(ir.IntType(1)(0), result)
            return self.builder.load(result), result

    # Visit a parse tree produced by tinycParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx: tinycParser.LogicalOrExpressionContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.logicalAndExpression())
        else:
            lhs = (self.visit(ctx.children[0])[0])
            result = self.builder.alloca(ir.IntType(1))
            converted = whether_is_true(self.builder, lhs)
            cond = LLVMTypes.bool(converted.get_reference())
            with self.builder.if_else(cond) as (then, otherwise):
                with then:
                    self.builder.store(ir.IntType(1)(1), result)
                with otherwise:
                    rhs, rhs_ptr = self.visit(ctx.logicalAndExpression())
                    converted_rhs = whether_is_true(self.builder, rhs)
                    self.builder.store(converted_rhs, result)
            return self.builder.load(result), result

    # Visit a parse tree produced by tinycParser#conditionalExpression.
    def visitConditionalExpression(self, ctx: tinycParser.ConditionalExpressionContext):
        return self.visit(ctx.logicalOrExpression())

    # Visit a parse tree produced by tinycParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx: tinycParser.AssignmentOperatorContext):
        return ctx.getText()

    # Visit a parse tree produced by tinycParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:tinycParser.PrimaryExpressionContext):
        """return val and addr"""
        if ctx.IDENTIFIER():
            text = ctx.getText()
            addr = self.symbol_table.getSymbol(text)
            if addr:
                print("primary of addr",type(addr), addr)
                if type(addr) in [ir.Argument, ir.Function]:
                    print("why it is not ", addr)
                    #TODO:here is a function parameter bug
                    return addr, addr
                elif isinstance(addr.type.pointee, ir.ArrayType):
                    zero = ir.Constant(LLVMTypes.int, 0)
                    value = self.builder.gep(addr, [zero, zero])
                else:
                    print(f"{text}addr is ", addr)
                    value = self.builder.load(addr)
                return value, addr
            else:
                raise Exception('the identifier should be defined first')
        elif ctx.mString():
            text = self.visit(ctx.mString())
            idx = self.constants
            self.constants += 1
            text = text[1:-1]
            strlen = len(text) + 1
            print(f'strlen {strlen}')
            string = get_const_from_str('string', text)
            # print(string)
            # const = ir.GlobalVariable(self.module, ir.ArrayType(LLVMTypes.int8,strlen), ".str%d"%idx)
            # const.global_constant = True
            # const.initializer = string
            # zero = ir.Constant(LLVMTypes.int32, 0)
            # first = ir.Constant(ir.ArrayType, bytearray( ,'ascii'))
            return string, string
        elif ctx.CONSTANT():
            text = ctx.getText()
            print('const', text)
            const = get_const_from_str('int', text)
            return const, None
        elif ctx.expression():
            val = self.visit(ctx.expression())
            return val , None
        else:
            raise Exception('not supported')

    def visitMString(self, ctx:tinycParser.MStringContext):
        """ 将string或者char里面的\n修改了"""
        text = ctx.getText()
        text = formatString(text)
        return text
