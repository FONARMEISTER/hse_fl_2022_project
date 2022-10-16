# Generated from arithmetic.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .arithmeticParser import arithmeticParser
else:
    from arithmeticParser import arithmeticParser

# This class defines a complete generic visitor for a parse tree produced by arithmeticParser.

class arithmeticVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by arithmeticParser#file_.
    def visitFile_(self, ctx:arithmeticParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#PowExpr.
    def visitPowExpr(self, ctx:arithmeticParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#MultExpr.
    def visitMultExpr(self, ctx:arithmeticParser.MultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#BracketExpr.
    def visitBracketExpr(self, ctx:arithmeticParser.BracketExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#AtomExpr.
    def visitAtomExpr(self, ctx:arithmeticParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#SumExpr.
    def visitSumExpr(self, ctx:arithmeticParser.SumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by arithmeticParser#atom.
    def visitAtom(self, ctx:arithmeticParser.AtomContext):
        return self.visitChildren(ctx)



del arithmeticParser