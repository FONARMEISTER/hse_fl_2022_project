from pspLexer import pspLexer
from pspListener import pspListener
from pspParser import pspParser
from antlr4 import *
import sys
import time
import os
import os.path

class pspCounter(pspListener):
    def __init__(self):
        self.roundOpen = 0
        self.roundClose = 0
        self.squareOpen = 0
        self.squareClose = 0
        self.PSPcount = 0
    
    def enterLrp(self, ctx: pspParser.LrpContext):
        self.roundOpen += 1
    
    def enterRrp(self, ctx: pspParser.RrpContext):
        self.roundClose += 1

    def enterLsp(self, ctx: pspParser.LspContext):
        self.squareOpen += 1

    def enterRsp(self, ctx: pspParser.RspContext):
        self.squareClose += 1

    def exitExpression(self, ctx: pspParser.ExpressionContext):
        self.PSPcount += 1

def main():
    sys.setrecursionlimit(2000000)
    start_time = time.time()
    lexer = pspLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = pspParser(stream)
    tree = parser.file_()
    #print('Parse Tree building time :', time.time() - start_time, 'seconds')
    #start_time = time.time()
    #walker = ParseTreeWalker()
    #counter = pspCounter()
    #walker.walk(counter, tree)
    #print('Walking time:', time.time() - start_time, 'seconds')

if __name__ == '__main__':
    main()
