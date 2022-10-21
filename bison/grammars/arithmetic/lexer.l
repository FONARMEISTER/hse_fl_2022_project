%{
    /* definitions */
    #include "parser.tab.h"
%}

/* rules */
%%

(-)?[0-9]+ { yylval.num = atoi(yytext); return NUMBER; }
"+" { return PLUS; }
"-" { return MINUS; }
"*" { return MULT; }
"/" { return DIV; }
"^" { return POW; }
"(" { return LPAREN; }
")" {return RPAREN; }
\n {return EOL;}
[ \t] {}
