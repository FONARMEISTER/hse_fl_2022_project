#!/bin/bash

lex lexer.l
byacc -d parser.y
gcc -o calc lex.yy.c y.tab.c -lfl -lm


for filename in $(ls tests) ; do
  { time ./calc < tests/"$filename" ;} > output/"$filename".res 2> output/"$filename".time
done