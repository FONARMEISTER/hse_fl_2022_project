import ply.lex as lex
import sys
import os

tokens = [
    "NUM",
    "PLUS",
    "MINUS",
    "POW",
    "MULT",
    "DIV",
    "LPAREN",
    "RPAREN"
]

def t_NUM(t) :
    r'[0-9]+'
    t.value = int(t.value)
    return t

t_PLUS = r'\+'
t_MINUS = r'\-'
t_POW = r'\^'
t_MULT = r'\*'
t_DIV = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

def test():
    from pathlib import Path
    dir = os.getcwd() + '/test-in'
    #print(os.listdir(dir))
    for file in os.listdir(dir):
        with open(dir + '/' + file, 'r') as fin, open(os.getcwd() + '/test-out/' + file + '.out', 'w') as fout:
            text = fin.read()
            print(text)
            origin = sys.stdout
            sys.stdout = fout

            lexer.input(text)

            while True:
              tok = lexer.token()
              if not tok:
                break
              print(tok)
        
            sys.stdout = origin


def main():
  lexer = lex.lex()
  if sys.argv[1] == '--test':
    test()
    return


  lexer.input(sys.argv[1])

  while True:
    tok = lexer.token()
    if not tok:
      break
    print(tok)

if __name__ == "__main__":
    main()
