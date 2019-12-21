from preprocess.CmacrosVisitor import CmacrosVisitor, CmacrosParser

class MacroVisitor(CmacrosVisitor):

    def __init__(self):
        self.macros = {}

    # Visit a parse tree produced by CmacrosParser#program.
    def visitProgram(self, ctx:CmacrosParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#translation_unit.
    def visitTranslation_unit(self, ctx:CmacrosParser.Translation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#preprocessor.
    def visitPreprocessor(self, ctx:CmacrosParser.PreprocessorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#pp_define.
    def visitPp_define(self, ctx:CmacrosParser.Pp_defineContext):

        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#pp_ignore.
    def visitPp_ignore(self, ctx:CmacrosParser.Pp_ignoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#token_sequence.
    def visitToken_sequence(self, ctx:CmacrosParser.Token_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CmacrosParser#ignore.
    def visitIgnore(self, ctx:CmacrosParser.IgnoreContext):
        print(ctx.ID().getText())
        for i in ctx.children:
            print(i.getText(), ' ')
        return self.visitChildren(ctx)

