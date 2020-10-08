### Challenge Name

Foo Bar Baz

### Description

Just print a series of numbers... but there are some caveats.

### Problem Statement

Input consists of 4 numbers, $n$, $m$, $x$, $y$. Print every number from $n$ to
$m$ (inclusive) unless it meets the following conditions:

* if the number is divisible by x, print "foo" instead of the number
* if the number is divisible by y, print "bar" instead of the number
* if the number is divisible by x and y, print "baz" instead of the number

### Input Format

$n$	$m$	$x$	$y$

Values are separated by tabs.

N.B. there is no tab follwing $y$, only a newline.

### Constraints

$0 \lt n,m \lt 100$

$n \le m$

$1 \lt x,y \lt 11$

$x \ne y$

### Output Format

$o_1$

$o_2$

$\vdots$

$o_n$

Where $o_i$ represents an output (a number, "foo", "bar", or "baz").

One output per line.

### Tags
