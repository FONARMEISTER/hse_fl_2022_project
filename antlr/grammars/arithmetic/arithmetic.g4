grammar arithmetic;

file_ : expression* EOF;

expression     :  expression  POW expression #PowExpr
               |  expression  MULT_SIGN  expression #MultExpr
               |  expression  SUM_SIGN expression #SumExpr
               |  LPAREN expression RPAREN #BracketExpr
               |  atom #AtomExpr ;

atom     : NUMBER;

NUMBER   : '-'? ('0' .. '9')+ ;

SUM_SIGN     : (PLUS | MINUS) ;

MULT_SIGN    : (TIMES | DIV) ;  

LPAREN   : '(' ;

RPAREN   : ')' ;

fragment PLUS     : '+' ;

fragment MINUS    : '-' ;

fragment TIMES    : '*' ;

fragment DIV      : '/' ;

POW      : '^' ;

WS       : [ \r\n\t] + -> skip ;