%{
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
%}

%union {
    char *str;
}

%type<str> s
%token<str> LSQUAREPAREN RSQUAREPAREN LROUNDPAREN RROUNDPAREN END
%token EOL

/* rules */
%start Input
%%

Input:

     | Input line
;

line:
    s END { printf("%s\n", $1); }
|   EOL
;

s:  LROUNDPAREN s RROUNDPAREN s { $$ = yylval.str; }
|   LROUNDPAREN s RROUNDPAREN { $$ = yylval.str; }
|   LROUNDPAREN RROUNDPAREN s { $$ = yylval.str; }
|   LROUNDPAREN RROUNDPAREN { $$ = "()"; }
|   LSQUAREPAREN s RSQUAREPAREN s { $$ = yylval.str; }
|   LSQUAREPAREN s RSQUAREPAREN { $$ = yylval.str; }
|   LSQUAREPAREN RSQUAREPAREN s { $$ = yylval.str; }
|   LSQUAREPAREN RSQUAREPAREN { $$ = "[]"; }
;

%%

int main() {
    yyparse();
}

yyerror(char* s) {
    printf("ERROR: %s\n", s);
}
