grammar psp;

file_ : expression* EOF;

expression      : S;

S       : S1'('S')'
        | ;

S1      : S'['S']' 
        | ;

WS       : [ \r\n\t] + -> skip ;