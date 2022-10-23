from arithmetic2Lexer import arithmetic2Lexer
from arithmetic2Parser import arithmetic2Parser
from arithmetic2Visitor import arithmetic2Visitor
from antlr4 import *
import sys
import time
import os
import os.path

class arithmeticsEvaluator(arithmetic2Visitor):

    def visitFile_(self, ctx: arithmetic2Parser.File_Context):
        for expr in ctx.children:
            print(self.visit(expr))
    
    def visitExprSum(self, ctx: arithmetic2Parser.ExprSumContext):
        res = self.visit(ctx.children[0])
        for i in range(1, len(ctx.children), 2):
            op = ctx.children[i].getText()
            term = self.visit(ctx.children[i + 1])
            if op == "+":
                res += term
            else:
                res -= term
        return res
    
    def visitTermMult(self, ctx: arithmetic2Parser.TermMultContext):
        res = self.visit(ctx.children[0])
        for i in range(1, len(ctx.children), 2):
            op = ctx.children[i].getText()
            term = self.visit(ctx.children[i + 1])
            if op == "*":
                res *= term
            else:
                res //= term
        return res

    def visitFactorPow(self, ctx: arithmetic2Parser.FactorPowContext):
        atom = self.visit(ctx.children[0])
        if len(ctx.children) == 1:
            return atom
        factor = self.visit(ctx.children[2])
        return atom ** factor

    def visitAtomExpr(self, ctx: arithmetic2Parser.AtomExprContext):
        return self.visit(ctx.children[1])
        
    def visitAtomNum(self, ctx: arithmetic2Parser.AtomNumContext):
        return int(ctx.NUMBER().getText())
        

def main():
    sys.setrecursionlimit(2000000)
    start_time = time.time()
    lexer = arithmetic2Lexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = arithmetic2Parser(stream)
    tree = parser.file_()
    #print('Parse Tree building time :', time.time() - start_time, 'seconds')
    start_time = time.time()
    #for exprs in tree.children:
    #    result = arithmeticsEvaluator().visit(exprs)
    #print('Evaluating time:', time.time() - start_time, 'seconds')
    #print()


if __name__ == '__main__':
    main()
