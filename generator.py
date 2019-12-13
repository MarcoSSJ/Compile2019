from parser_.tinycLexer import tinycLexer
from parser_.tinycListener import tinycListener
from parser_.tinycParser import tinycParser
from antlr4 import *
import llvmlite.ir as ir
class generativeListener(tinycListener):
    def __init__(self):
        pass

    def enterProgram(self, ctx: tinycParser.ProgramContext):
        print("enter")
        pass

        # Exit a parse tree produced by tinycParser#program.

    def exitProgram(self, ctx: tinycParser.ProgramContext):
        pass

        # Enter a parse tree produced by tinycParser#statement.

    def enterStatement(self, ctx: tinycParser.StatementContext):
        pass

        # Exit a parse tree produced by tinycParser#statement.

    def exitStatement(self, ctx: tinycParser.StatementContext):
        pass

        # Enter a parse tree produced by tinycParser#paren_expr.

    def enterParen_expr(self, ctx: tinycParser.Paren_exprContext):
        pass

        # Exit a parse tree produced by tinycParser#paren_expr.

    def exitParen_expr(self, ctx: tinycParser.Paren_exprContext):
        pass

        # Enter a parse tree produced by tinycParser#expr.

    def enterExpr(self, ctx: tinycParser.ExprContext):
        if len(ctx.children == 1):
            v = self.enterTest(ctx.test())
            print(v)
            return v
        pass

        # Exit a parse tree produced by tinycParser#expr.

    def exitExpr(self, ctx: tinycParser.ExprContext):
        pass

        # Enter a parse tree produced by tinycParser#test.

    def enterTest(self, ctx: tinycParser.TestContext):
        if len(ctx.children == 1):
            v = self.enterSta_sum(ctx.sta_sum())
            return v
        pass

        # Exit a parse tree produced by tinycParser#test.

    def exitTest(self, ctx: tinycParser.TestContext):
        pass

        # Enter a parse tree produced by tinycParser#sta_sum.

    def enterSta_sum(self, ctx: tinycParser.Sta_sumContext):
        if len(ctx.children == 1):
            v = self.enterTerm(ctx.term())
            return v
        pass

        # Exit a parse tree produced by tinycParser#sta_sum.

    def exitSta_sum(self, ctx: tinycParser.Sta_sumContext):
        pass

        # Enter a parse tree produced by tinycParser#term.

    def enterTerm(self, ctx: tinycParser.TermContext):
        pass

        # Exit a parse tree produced by tinycParser#term.

    def exitTerm(self, ctx: tinycParser.TermContext):
        pass

        # Enter a parse tree produced by tinycParser#exp_id.

    def enterExp_id(self, ctx: tinycParser.Exp_idContext):
        pass

        # Exit a parse tree produced by tinycParser#exp_id.

    def exitExp_id(self, ctx: tinycParser.Exp_idContext):
        pass

        # Enter a parse tree produced by tinycParser#integer.

    def enterInteger(self, ctx: tinycParser.IntegerContext):
        print(ctx.children[0])
        pass

        # Exit a parse tree produced by tinycParser#integer.

    def exitInteger(self, ctx: tinycParser.IntegerContext):
        pass

def main(filename, output):
    input_stream = FileStream(filename)
    lexer = tinycLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = tinycParser(token_stream)
    # Entry point in the json g4 grammar: json
    tree = parser.program()
    my_listener = generativeListener()
    walker = ParseTreeWalker()
    walker.walk(my_listener, tree)


main('test.c','output.c')