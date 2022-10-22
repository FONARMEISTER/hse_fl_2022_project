%{
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define YYINITDEPTH 1000000
#define YYMAXDEPTH 10000000
%}

%union {
    int num;
    char sym;
}

%token EOL
%token<num> NUMBER
%type<num> expr
%type<num> term
%type<num> factor
%type<num> atom
%token PLUS MINUS MULT LPAREN RPAREN DIV POW

%left PLUS MINUS
%left MULT DIV
%right POW



/* rules */
%start Input
%%

Input:

     | Input line
;

line:
    expr EOL { printf("%d\n", $1); }
|   EOL
;

expr:
    term { $$ = $1; }
|   expr PLUS term {  $$ = $1 + $3; }
|   expr MINUS term { $$ = $1 - $3; }
;

term:
    factor { $$ = $1; }
|   term MULT factor { $$ = $1 * $3; }
|   term DIV factor { $$ = $1 / $3; }
;

factor:
    atom { $$ = $1; }
|   atom POW factor { $$ = pow($1, $3); }
;

atom:
    LPAREN expr RPAREN { $$ = $2; }
|   NUMBER { $$ = $1; }

%%

int main() {
    yyparse();
}

yyerror(char* s) {
    printf("ERROR: %s\n", s);
}
