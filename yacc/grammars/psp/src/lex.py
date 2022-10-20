import ply.lex as lex
import sys
import os


tokens = [
    "LPR",
    "RPR",
    "LPS",
    "RPS"
]

t_LPR = r'\('
t_RPR = r'\)'
t_LPS = r'\['
t_RPS = r'\]'

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()







