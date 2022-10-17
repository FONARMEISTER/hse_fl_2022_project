grammar psp;

file_ : expression* EOF;

expression      : s';';

s       : lrp s? rrp s? 
        | lsp s? rsp s? ;
        

lrp     : LROUNDPAREN ;

rrp     : RROUNDPAREN ;

lsp     : LSQUAREPAREN ;

rsp     : RSQUAREPAREN ;

LROUNDPAREN     : '(' ;

RROUNDPAREN     : ')' ;

LSQUAREPAREN    : '[' ;

RSQUAREPAREN    : ']' ;

WS       : [ \r\n\t] + -> skip ;