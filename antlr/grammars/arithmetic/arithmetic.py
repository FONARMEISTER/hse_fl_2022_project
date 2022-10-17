from arithmeticLexer import arithmeticLexer
from arithmeticParser import arithmeticParser
from arithmeticVisitor import arithmeticVisitor
from antlr4 import *
import sys
import time
import os
import os.path

class arithmeticsEvaluator(arithmeticVisitor):

    def visitFile_(self, ctx: arithmeticParser.File_Context):
        for expr in ctx.children:
            print(self.visit(expr))
    
    def visitBracketExpr(self, ctx: arithmeticParser.BracketExprContext):
        return self.visit(ctx.children[1])
    
    def visitMultExpr(self, ctx: arithmeticParser.MultExprContext):
        expr1 = self.visit(ctx.children[0])
        expr2 = self.visit(ctx.children[2])
        op = ctx.children[1].getText()
        if op == "*":
            return expr1 * expr2
        else:
            return expr1 // expr2

    def visitPowExpr(self, ctx: arithmeticParser.PowExprContext):
        expr1 = self.visit(ctx.children[0])
        expr2 = self.visit(ctx.children[2])
        return expr1 ** expr2

    def visitSumExpr(self, ctx: arithmeticParser.MultExprContext):
        expr1 = self.visit(ctx.children[0])
        expr2 = self.visit(ctx.children[2])
        op = ctx.children[1].getText()
        if op == "+":
            return expr1 + expr2
        else:
            return expr1 - expr2

    def visitAtomExpr(self, ctx: arithmeticParser.AtomExprContext):
        return int(ctx.atom().getText())
        

def main():
    sys.setrecursionlimit(2000000)
    tests_dir = os.path.join(os.getcwd(), 'tests')
    tests = os.listdir(tests_dir)
    test_count = 0
    for test in tests:
        test_count += 1
        print('Test', os.path.splitext(test)[0])
        start_time = time.time()
        lexer = arithmeticLexer(FileStream(os.path.join(tests_dir, test)))
        stream = CommonTokenStream(lexer)
        parser = arithmeticParser(stream)
        tree = parser.file_()
        print('Parse Tree building time :', time.time() - start_time, 'seconds')
        if ('Large' in test):
            print()
            continue
        out_path = os.path.join(os.getcwd(), 'output', os.path.splitext(test)[0] + '.out')
        with open(out_path, "w") as out:
            start_time = time.time()
            for exprs in tree.children:
                result = arithmeticsEvaluator().visit(exprs)
                if result != None:
                    out.write(str(result) + '\n')
        print('Evaluating time:', time.time() - start_time, 'seconds')
        print()


if __name__ == '__main__':
    main()
