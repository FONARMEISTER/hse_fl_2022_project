#!/bin/bash

function put_tests_together {
  for filename in $(ls "$1"tests) ; do
    echo "      YACC:   " > "$1"output-summary/"$filename".sum
    cat "$1"output-yacc/"$filename".time >> "$1"output-summary/"$filename".sum
    echo "====================" >> "$1"output-summary/"$filename".sum
    echo "      BISON:   " >> "$1"output-summary/"$filename".sum
    cat "$1"output-bison/"$filename".time >> "$1"output-summary/"$filename".sum
    echo "====================" >> "$1"output-summary/"$filename".sum
    echo "      ANTLR:   " >> "$1"output-summary/"$filename".sum
    cat "$1"output-antlr/"$filename".time >> "$1"output-summary/"$filename".sum
  done
}

#tester -------------------------------------------------------

lex yacc-c/grammars/arithmetic/lexer.l
byacc -d yacc-c/grammars/arithmetic/parser.y
gcc -o calc lex.yy.c y.tab.c -lfl -lm

path="grammars/arithmetic/"

for filename in $(ls "$path"tests) ; do
  { time ./calc < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-yacc/"$filename".time
done

flex bison/grammars/arithmetic/lexer.l
bison -d bison/grammars/arithmetic/parser.y
gcc -o calc lex.yy.c parser.tab.c -lfl -lm


for filename in $(ls "$path"tests) ; do
  { time ./calc < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-bison/"$filename".time
done

antlr4 -Dlanguage=Python3 -visitor antlr/grammars/arithmetic/arithmetic.g4

for filename in $(ls "$path"tests) ; do
  { time pypy3 antlr/grammars/arithmetic/arithmetic.py < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-antlr/"$filename".time
done


#write here arithm1

put_tests_together $path

#--------------------------------------------------------

lex yacc-c/grammars/arithmetic2/lexer.l
byacc -d yacc-c/grammars/arithmetic2/parser.y
gcc -o calc lex.yy.c y.tab.c -lfl -lm

path="grammars/arithmetic2/"

for filename in $(ls "$path"tests) ; do
  { time ./calc < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-yacc/"$filename".time
done

flex bison/grammars/arithmetic2/lexer.l
bison -d bison/grammars/arithmetic2/parser.y
gcc -o calc lex.yy.c parser.tab.c -lfl -lm


for filename in $(ls "$path"tests) ; do
  { time ./calc < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-bison/"$filename".time
done


antlr4 -Dlanguage=Python3 -visitor antlr/grammars/arithmetic2/arithmetic2.g4

for filename in $(ls "$path"tests) ; do
  { time pypy3 antlr/grammars/arithmetic2/arithmetic2.py < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-antlr/"$filename".time
done
#write here arithm2

put_tests_together $path


#------------------------------------------------------------

lex yacc-c/grammars/psp/lexer.l
byacc -d yacc-c/grammars/psp/parser.y
gcc -o calc lex.yy.c y.tab.c -lfl -lm

path="grammars/psp/"

for filename in $(ls "$path"tests) ; do
  { time ./calc < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-yacc/"$filename".time
done

flex bison/grammars/psp/lexer.l
bison -d bison/grammars/psp/parser.y
gcc -o calc lex.yy.c parser.tab.c -lfl -lm

for filename in $(ls "$path"tests) ; do
  { time ./calc < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-bison/"$filename".time
done


antlr4 -Dlanguage=Python3 -visitor antlr/grammars/psp/psp.g4

for filename in $(ls "$path"tests) ; do
  { time pypy3 antlr/grammars/psp/psp.py < "$path"tests/"$filename" ;} > /dev/null 2> "$path"output-antlr/"$filename".time
done

# write here psp

put_tests_together $path





