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


    # Enter a parse tree produced by tinycParser#statement.
    def enterStatement(self, ctx:tinycParser.StatementContext):
        pass

    # Exit a parse tree produced by tinycParser#statement.
    def exitStatement(self, ctx:tinycParser.StatementContext):
        pass


    # Enter a parse tree produced by tinycParser#paren_expr.
    def enterParen_expr(self, ctx:tinycParser.Paren_exprContext):
        pass

    # Exit a parse tree produced by tinycParser#paren_expr.
    def exitParen_expr(self, ctx:tinycParser.Paren_exprContext):
        pass


    # Enter a parse tree produced by tinycParser#expr.
    def enterExpr(self, ctx:tinycParser.ExprContext):
        pass

    # Exit a parse tree produced by tinycParser#expr.
    def exitExpr(self, ctx:tinycParser.ExprContext):
        pass


    # Enter a parse tree produced by tinycParser#test.
    def enterTest(self, ctx:tinycParser.TestContext):
        pass

    # Exit a parse tree produced by tinycParser#test.
    def exitTest(self, ctx:tinycParser.TestContext):
        pass


    # Enter a parse tree produced by tinycParser#sta_sum.
    def enterSta_sum(self, ctx:tinycParser.Sta_sumContext):
        pass

    # Exit a parse tree produced by tinycParser#sta_sum.
    def exitSta_sum(self, ctx:tinycParser.Sta_sumContext):
        pass


    # Enter a parse tree produced by tinycParser#term.
    def enterTerm(self, ctx:tinycParser.TermContext):
        pass

    # Exit a parse tree produced by tinycParser#term.
    def exitTerm(self, ctx:tinycParser.TermContext):
        pass


    # Enter a parse tree produced by tinycParser#exp_id.
    def enterExp_id(self, ctx:tinycParser.Exp_idContext):
        pass

    # Exit a parse tree produced by tinycParser#exp_id.
    def exitExp_id(self, ctx:tinycParser.Exp_idContext):
        pass


    # Enter a parse tree produced by tinycParser#integer.
    def enterInteger(self, ctx:tinycParser.IntegerContext):
        pass

    # Exit a parse tree produced by tinycParser#integer.
    def exitInteger(self, ctx:tinycParser.IntegerContext):
        pass


