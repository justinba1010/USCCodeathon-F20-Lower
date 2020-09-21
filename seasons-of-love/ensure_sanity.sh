#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

NUM_TESTS=$(ls input | sort -V | tail -1 | grep -o '[0-9]\+')
MY_TMP="$(mktemp -dt tmp.XXXX)"

ensure_solution () {
	case $1 in
		*.java) printf "cd solutions; java $(javac -verbose $1 2>&1 | tail -2 | head -1 | sed 's#.*solutions/\(.*\)\.class.*#\1#')";;
		*.c) gcc -O3 $solution -o solutions/solution_c; printf "solutions/solution_c";;
		*.hs) ghc -O3 -outputdir "$MY_TMP" $solution -o solutions/solution_hs >/dev/null
			printf "solutions/solution_hs"
			rm -rf "$MY_TMP";;
		*.rs) if [ -e solutions/Cargo.toml ]; then
			cd solutions
			ln -sf target/release/solution_rs
			cargo build --release
		else
			rustc -O $solution -o solutions/solution_rs
		fi
		printf solutions/solution_rs;;
		*) printf "%s" "$1";;
	esac
}

for solution in solutions/solution.*; do
	solution="$(ensure_solution $solution)"
	echo "trying solution $solution"
	for i in $(seq 1 $NUM_TESTS); do
		[ "$(cat output/output$i.txt)" = "$(eval "$solution" < input/input$i.txt)" ] || {
			echo failed on test $i
			exit 1
		}
	done
done
echo success
