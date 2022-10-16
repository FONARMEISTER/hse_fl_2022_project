# Generated from arithmetic.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .arithmeticParser import arithmeticParser
else:
    from arithmeticParser import arithmeticParser

# This class defines a complete listener for a parse tree produced by arithmeticParser.
class arithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by arithmeticParser#file_.
    def enterFile_(self, ctx:arithmeticParser.File_Context):
        pass

    # Exit a parse tree produced by arithmeticParser#file_.
    def exitFile_(self, ctx:arithmeticParser.File_Context):
        pass


    # Enter a parse tree produced by arithmeticParser#PowExpr.
    def enterPowExpr(self, ctx:arithmeticParser.PowExprContext):
        pass

    # Exit a parse tree produced by arithmeticParser#PowExpr.
    def exitPowExpr(self, ctx:arithmeticParser.PowExprContext):
        pass


    # Enter a parse tree produced by arithmeticParser#MultExpr.
    def enterMultExpr(self, ctx:arithmeticParser.MultExprContext):
        pass

    # Exit a parse tree produced by arithmeticParser#MultExpr.
    def exitMultExpr(self, ctx:arithmeticParser.MultExprContext):
        pass


    # Enter a parse tree produced by arithmeticParser#BracketExpr.
    def enterBracketExpr(self, ctx:arithmeticParser.BracketExprContext):
        pass

    # Exit a parse tree produced by arithmeticParser#BracketExpr.
    def exitBracketExpr(self, ctx:arithmeticParser.BracketExprContext):
        pass


    # Enter a parse tree produced by arithmeticParser#AtomExpr.
    def enterAtomExpr(self, ctx:arithmeticParser.AtomExprContext):
        pass

    # Exit a parse tree produced by arithmeticParser#AtomExpr.
    def exitAtomExpr(self, ctx:arithmeticParser.AtomExprContext):
        pass


    # Enter a parse tree produced by arithmeticParser#SumExpr.
    def enterSumExpr(self, ctx:arithmeticParser.SumExprContext):
        pass

    # Exit a parse tree produced by arithmeticParser#SumExpr.
    def exitSumExpr(self, ctx:arithmeticParser.SumExprContext):
        pass


    # Enter a parse tree produced by arithmeticParser#atom.
    def enterAtom(self, ctx:arithmeticParser.AtomContext):
        pass

    # Exit a parse tree produced by arithmeticParser#atom.
    def exitAtom(self, ctx:arithmeticParser.AtomContext):
        pass



del arithmeticParser