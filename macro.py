from preprocess.CmacrosVisitor import CmacrosVisitor
from preprocess.CmacrosParser import CmacrosParser
from MacroTable import MacroList, MacroTable
class MacroVisitor(CmacrosVisitor):

    def __init__(self, table: MacroTable):
        self.macros = {}
        self.table = table

    # Visit a parse tree produced by CmacrosParser#program.
    def visitProgram(self, ctx:CmacrosParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitBody(self, ctx: CmacrosParser.BodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CmacrosParser#translation_unit.
    def visitTranslation_unit(self, ctx:CmacrosParser.Translation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#preprocessor.
    def visitPreprocessor(self, ctx:CmacrosParser.PreprocessorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#pp_define.
    def visitPp_define(self, ctx:CmacrosParser.Pp_defineContext):
        mlist = MacroList()
        first = True
        for i in ctx.ID():
            if first:
                self.table.table[i.getText()] = mlist
            else:
                mlist.params[i.getText()] = None
        mlist.tokens = self.visit(ctx.token_sequence())
        print(len(mlist.params))
        print(len(mlist.tokens))
        # print(ctx.token_sequence().getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#pp_ignore.
    def visitPp_ignore(self, ctx:CmacrosParser.Pp_ignoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#token_sequence.
    def visitToken_sequence(self, ctx:CmacrosParser.Token_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#ignore.
    def visitIgnore(self, ctx:CmacrosParser.IgnoreContext):
        # for i in ctx.ID():
        #     print("define ID", i.getText())
        token_list = []
        for i in ctx.children:
            token_list.append(i.getText())
            # print(i.getText(), 'children')
        return token_list

