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

s:  LROUNDPAREN s RROUNDPAREN s { $$ = strcat(); }
|   LSQUAREPAREN s RSQUAREPAREN s { }
|
;

%%

int main() {
    yyparse();
}

yyerror(char* s) {
    printf("ERROR: %s\n", s);
}
