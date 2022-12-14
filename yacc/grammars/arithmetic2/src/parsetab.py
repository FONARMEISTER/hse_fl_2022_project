
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIV LPAREN MINUS MULT NUM PLUS POW RPARENexpr : term \n          | term PLUS exprexpr : term MINUS exprterm : factor\n          | factor MULT termterm  : factor DIV termfactor : atom\n            | atom POW factoratom : LPAREN expr RPAREN\n            | NUM'
    
_lr_action_items = {'LPAREN':([0,5,7,8,9,10,11,],[5,5,5,5,5,5,5,]),'NUM':([0,5,7,8,9,10,11,],[6,6,6,6,6,6,6,]),'$end':([1,2,3,4,6,13,14,15,16,17,18,],[0,-1,-4,-7,-10,-2,-3,-5,-6,-8,-9,]),'RPAREN':([2,3,4,6,12,13,14,15,16,17,18,],[-1,-4,-7,-10,18,-2,-3,-5,-6,-8,-9,]),'PLUS':([2,3,4,6,15,16,17,18,],[7,-4,-7,-10,-5,-6,-8,-9,]),'MINUS':([2,3,4,6,15,16,17,18,],[8,-4,-7,-10,-5,-6,-8,-9,]),'MULT':([3,4,6,17,18,],[9,-7,-10,-8,-9,]),'DIV':([3,4,6,17,18,],[10,-7,-10,-8,-9,]),'POW':([4,6,18,],[11,-10,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,5,7,8,],[1,12,13,14,]),'term':([0,5,7,8,9,10,],[2,2,2,2,15,16,]),'factor':([0,5,7,8,9,10,11,],[3,3,3,3,3,3,17,]),'atom':([0,5,7,8,9,10,11,],[4,4,4,4,4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> term','expr',1,'p_expr_plus','parse.py',11),
  ('expr -> term PLUS expr','expr',3,'p_expr_plus','parse.py',12),
  ('expr -> term MINUS expr','expr',3,'p_expr_minus','parse.py',16),
  ('term -> factor','term',1,'p_term_mult','parse.py',20),
  ('term -> factor MULT term','term',3,'p_term_mult','parse.py',21),
  ('term -> factor DIV term','term',3,'p_term_div','parse.py',25),
  ('factor -> atom','factor',1,'p_factor','parse.py',29),
  ('factor -> atom POW factor','factor',3,'p_factor','parse.py',30),
  ('atom -> LPAREN expr RPAREN','atom',3,'p_atom','parse.py',34),
  ('atom -> NUM','atom',1,'p_atom','parse.py',35),
]
