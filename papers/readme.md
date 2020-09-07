# Donald's Papers

## Description

Dr. Knuth needs to find the average and median of all of his papers.

## Problem Statement

Dr. Knuth needs to find the average and median of his class as a letter grade. Below are the grades to table.


| lower | higher | letter grade |
| --- | --- | --- | --- |
| 90 | 100 | A |
| 80 | 90 | B |
| 70 | 80 | C |
| 60 | 70 | D |
| 0 | 60 | F |

These couples are $(lower, higher]$, as in a 90 is an A, but a 89.999 is a B.
His class grades will be given in a single line space separated.

Medians are generated just as in normal statistics, where if `n` is even it is the average of the middle 2 grades.

## Input Format

```
n
g_1 g_2 g_3 ... g_n
```

## Constraints

$0 \leq g_i \leq 100$  
$0 < n \leq 10000$

## Output Format

```
x y
```
where `x,y` are letter grades in the set $\{A,B,C,D,F\}$ and `x` is the average, and `y` is the median.
