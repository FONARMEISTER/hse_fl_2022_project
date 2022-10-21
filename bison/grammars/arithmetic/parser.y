%{
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define YYINITDEPTH 1000000
%}

%union {
    int num;
    char sym;
}

%token EOL
%token<num> NUMBER
%type<num> exp
%token PLUS MINUS MULT LPAREN RPAREN DIV POW

/* rules */
%start Input
%%

Input:

     | Input line
;

line:
    exp EOL { printf("%d\n", $1); }
|   EOL
;

exp:
    exp POW exp { $$ = pow($1, $3); }
|   exp MULT exp { $$ = $1 * $3; }
|   exp DIV exp { $$ = $1 / $3; }
|   exp PLUS exp { $$ = $1 + $3; }
|   exp MINUS exp { $$ = $1 - $3; }
|   LPAREN exp RPAREN { $$ = $2; }
|   NUMBER { $$ = $1; }
;
%%

int main() {
    yyparse();
}

yyerror(char* s) {
    printf("ERROR: %s\n", s);
}
