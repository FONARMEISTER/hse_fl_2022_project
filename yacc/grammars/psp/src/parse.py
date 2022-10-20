import ply.yacc as yacc

import sys
import re
import os
import time

from lex import tokens


def p_expr(p):
    '''expr : LPR expr RPR expr
            | LPS expr RPS expr
            | '''

def p_error(p):
  if p == None:
    token = "end of file"
    parser.errok()
  else:
    token = f"{p.type}({p.value}) on line {p.lineno}"

  print(f"Syntax error: Unexpected {token}")




def test():
    from pathlib import Path
    dir = os.getcwd() + '/test-in'
    #print(os.listdir(dir))
    for file in os.listdir(dir):
        with open(dir + '/' + file, 'r') as fin, open(os.getcwd() + '/test-out/' + file + '.out', 'w') as fout:
            text = fin.read()
            origin = sys.stdout
            sys.stdout = fout

            start_time = time.time()

            
            parser = yacc.yacc()
            print("parser build time is : " + str(time.time() - start_time) + " seconds")

            start_time = time.time()
            result = parser.parse(text)

            # print("result = " + str(result))
            print("parsing time is : " + str(time.time() - start_time) + " seconds")
            
        
            sys.stdout = origin


def main():
  parser = yacc.yacc()
  tm = time.time()
  if sys.argv[1] == '--test':
    test()
    print("total time is : " + str(time.time() - tm) + " seconds")
    return

  while True:
    try:
      s = input("calc> ")
    except EOFError:
      break
    if not s:
      continue
    result=parser.parse(s)
    print(result)

if __name__ == "__main__":
    main()
