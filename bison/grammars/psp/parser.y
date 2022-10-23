%{
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#define YYINITDEPTH 1000000
#define YYMAXDEPTH 10000000
%}

%union {
    char str;
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
    s END {  }
|   EOL
;

s:  LROUNDPAREN s RROUNDPAREN s {  }
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
