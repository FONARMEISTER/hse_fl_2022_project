grammar arithmetic2;

file_ : expression* EOF;

expression      :  term (SUM_SIGN term)* #ExprSum ;

term            : factor (MULT_SIGN factor)* #TermMult ;

factor          : atom (POW factor)? #FactorPow ;

atom            : LPAREN expression RPAREN #AtomExpr
                | NUMBER #AtomNum ; 

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