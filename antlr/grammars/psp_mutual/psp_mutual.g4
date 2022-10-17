grammar psp_mutual;

file_ : expression* EOF;

expression      : s;

s       : s1?'('s?')' ;

s1      : s?'['s?']' ;

WS       : [ \r\n\t] + -> skip ;