%{
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define YYINITDEPTH 1000000
%}

%token EOL
%token LSQUAREPAREN RSQUAREPAREN LROUNDPAREN RROUNDPAREN END

/* rules */
%start Input
%%

Input:

     | Input line
;

line:
    exp ';' EOL { printf("%d\n", $1); }
|   EOL
;

exp:
    '(' ')'
|   '[' ']'
|   '(' exp ')'
|   '[' exp ']'
;
%%

int main() {
    yyparse();
}

yyerror(char* s) {
    printf("ERROR: %s\n", s);
}
