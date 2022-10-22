%{
    /* definitions */
    #include "parser.tab.h"
%}

/* rules */
%%

"[" { yylval.str = strdup(yytext); return LSQUAREPAREN; }
"]" { yylval.str = strdup(yytext); return RSQUAREPAREN; }
"(" { yylval.str = strdup(yytext); return LROUNDPAREN; }
")" { yylval.str = strdup(yytext); return RROUNDPAREN; }
";" { return END; }
\n { return EOL; }
[ \t] {}
%%

