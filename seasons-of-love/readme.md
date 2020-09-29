# Seasons of Love

Angel and Tom are trying to get together for coffee.
Unfortunately, they're not very good at communicating.
Help them figure out when they should meet up!

## Input Format

The first line will contain a number of test cases $t$.
The following $t$ lines will have the format $n d$,
where $n$ is an integer and $d$ is one of the following strings:

- `s` for seconds
- `m` for minutes
- `h` for hours
- `d` for days
- `w` for weeks
- `mo` for months. For the purposes of this problem, assume there are always 30 days in a month.
- `y` for years

## Output format

Output the number of seconds $s$ until Angel and Tom meet up.

## Constraints

$1 \le t \le 200$
$1 \le s \le 2^32$

There are no constraints on $n$, other than that it is an integer and will not be so large it causes $s$ to be greater than $2^32$.

## Example Problem

### Input

525600 m

### Output

31536000

### Explanation

There are 60 seconds in a minute, so $525600*60$ is $31536000$ seconds.
