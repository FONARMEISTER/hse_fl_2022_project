import ply.yacc as yacc

import sys
import re
import os
import time

from lex import tokens

def p_expr_plus(p):
  '''expr : term 
          | term PLUS expr'''
  #p[0] = p[1] + p[3]

def p_expr_minus(p):
  '''expr : term MINUS expr'''
  #p[0] = p[1] - p[3]

def p_term_mult(p):
  '''term : factor
          | factor MULT term'''
  #p[0] = p[1] * p[3]

def p_term_div(p):
  '''term  : factor DIV term'''
  #p[0] = p[1] / p[3]

def p_factor(p):
  '''factor : atom
            | atom POW factor'''
  #p[0] = p[1] ** p[3]

def p_atom(p):
    '''atom : LPAREN expr RPAREN
            | NUM'''

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

          print("result = " + str(result))
          print("parsing time is : " + str(time.time() - start_time) + " seconds")
            
        
          sys.stdout = origin


def main():
  tm = time.time()
  if sys.argv[1] == '--test':
    test()
    print("total time is : " + str(time.time() - tm) + " seconds")
    return

if __name__ == "__main__":
    main()
