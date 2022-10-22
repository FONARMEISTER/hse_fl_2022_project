%{
    /* definitions */
    #include "y.tab.h"
%}

/* rules */
%%

"[" {  return LSQUAREPAREN; }
"]" {  return RSQUAREPAREN; }
"(" {  return LROUNDPAREN; }
")" {  return RROUNDPAREN; }
";" { return END; }
\n { return EOL; }
[ \t] {}
%%

