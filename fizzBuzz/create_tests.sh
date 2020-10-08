#!/bin/sh

# generate test cases for hackerrank

cd "$(dirname "$0")" || exit

mkdir -p input
mkdir -p output

make all

PAD='2'
n=0
while read -r line ; do
	num=$(printf "%0*d" "$PAD" "$n")
	INPUT_FILE="./input/input$num.txt"
	OUTPUT_FILE="./output/output$num.txt"
	echo "$line" > "$INPUT_FILE"
	./fizzbuzz_c.o > "$OUTPUT_FILE" < "$INPUT_FILE"
	n=$((n + 1))
done < testCases.tsv
