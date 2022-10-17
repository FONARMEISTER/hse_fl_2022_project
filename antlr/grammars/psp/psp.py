from pspLexer import pspLexer
from pspListener import pspListener
from pspParser import pspParser
from antlr4 import *
import sys
import time

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
    sys.setrecursionlimit(1000000)
    start_time = time.time()
    lexer = pspLexer(FileStream(sys.argv[1]))
    stream = CommonTokenStream(lexer)
    parser = pspParser(stream)
    tree = parser.file_()
    walker = ParseTreeWalker()
    counter = pspCounter()
    walker.walk(counter, tree)
    with open("output.txt", "w") as out:
        out.write('OpenRoundParen : ' + str(counter.roundOpen) + '\n')
        out.write('CloseRoundParen : ' + str(counter.roundClose) + '\n')
        out.write('OpenSquareParen : ' + str(counter.squareOpen) + '\n')
        out.write('CLoseSquareParen : ' + str(counter.squareClose) + '\n')
        out.write('PSP count : ' + str(counter.PSPcount) + '\n')
    print('Time:', time.time() - start_time, 'seconds')


if __name__ == '__main__':
    main()
