from arithmeticLexer import arithmeticLexer
from arithmeticListener import arithmeticListener
from arithmeticParser import arithmeticParser
from arithmeticVisitor import arithmeticVisitor
from antlr4 import *
import sys

class arithmeticsEvaulator(arithmeticVisitor):

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
    lexer = arithmeticLexer(FileStream(sys.argv[1]))
    stream = CommonTokenStream(lexer)
    parser = arithmeticParser(stream)
    tree = parser.file_()
    with open("output.txt", "w") as out:
        for exprs in tree.children:
            result = arithmeticsEvaulator().visit(exprs)
            if result != None:
                out.write(str(result) + '\n')


if __name__ == '__main__':
    main()
