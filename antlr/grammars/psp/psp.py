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
    tests_dir = os.path.join(os.getcwd(), 'tests')
    tests = os.listdir(tests_dir)
    test_count = 0
    for test in tests:
        test_count += 1
        print('Test', os.path.splitext(test)[0])
        start_time = time.time()
        lexer = pspLexer(FileStream(os.path.join(tests_dir, test)))
        stream = CommonTokenStream(lexer)
        parser = pspParser(stream)
        tree = parser.file_()
        print('Parse Tree building time :', time.time() - start_time, 'seconds')
        if ('Large' in test):
            print()
            continue
        start_time = time.time()
        walker = ParseTreeWalker()
        counter = pspCounter()
        walker.walk(counter, tree)
        print('Walking time:', time.time() - start_time, 'seconds')
        out_path = os.path.join(os.getcwd(), 'output', os.path.splitext(test)[0] + '.out')
        with open(out_path, "w") as out:
            out.write('OpenRoundParen : ' + str(counter.roundOpen) + '\n')
            out.write('CloseRoundParen : ' + str(counter.roundClose) + '\n')
            out.write('OpenSquareParen : ' + str(counter.squareOpen) + '\n')
            out.write('CLoseSquareParen : ' + str(counter.squareClose) + '\n')
            out.write('PSP count : ' + str(counter.PSPcount) + '\n')
        print()

if __name__ == '__main__':
    main()
