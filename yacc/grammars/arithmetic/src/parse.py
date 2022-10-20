import ply.yacc as yacc

import sys
import re
import os
import time

from lex import tokens

precedence = (
  ('left', 'PLUS', 'MINUS'),
  ('left', 'MULT', 'DIV'),
  ('right', 'POW')
)

def p_expr_plus(p):
  'expr : expr PLUS expr'
  #p[0] = p[1] + p[3]

def p_expr_minus(p):
  'expr : expr MINUS expr'
  #p[0] = p[1] - p[3]

def p_expr_mult(p):
  'expr : expr MULT expr'
  #p[0] = p[1] * p[3]

def p_expr_div(p):
  'expr : expr DIV expr'
  #p[0] = p[1] / p[3]

def p_expr_pow(p):
  'expr : expr POW expr'
  #p[0] = p[1] ** p[3]

def p_expr_num(p):
  '''expr : NUM
        | '''
  #p[0] = p[1]

def p_expr_br(p):
  'expr : LPAREN expr RPAREN'
  #p[0] = p[2]

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
