#!/bin/bash

#yacc-c tester

lex yacc-c/grammars/arithmetic/lexer.l
byacc -d yacc-c/grammars/arithmetic/parser.y
gcc -o calc lex.yy.c y.tab.c -lfl -lm

path="grammars/arithmetic/"

for filename in $(ls "$path"tests) ; do
  { time ./calc < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-yacc/"$filename".time
done

lex yacc-c/grammars/arithmetic2/lexer.l
byacc -d yacc-c/grammars/arithmetic2/parser.y
gcc -o calc lex.yy.c y.tab.c -lfl -lm

path="grammars/arithmetic2/"

for filename in $(ls "$path"tests) ; do
  { time ./calc < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-yacc/"$filename".time
done

lex yacc-c/grammars/psp/lexer.l
byacc -d yacc-c/grammars/psp/parser.y
gcc -o calc lex.yy.c y.tab.c -lfl -lm

path="grammars/psp/"

for filename in $(ls "$path"tests) ; do
  { time ./calc < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-yacc/"$filename".time
done
