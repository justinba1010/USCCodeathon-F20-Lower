#include <stdio.h>

int main (void) {
	unsigned int n, m, x, y;
	scanf("%u %u %u %u", &n, &m, &x, &y);

	for(;n<=m;n++) {
		if(n%x == 0 && n%y == 0) {
			printf("baz\n");
		}
		else if (n%y == 0) {
			printf("bar\n");
		}
		else if (n%x == 0) {
			printf("foo\n");
		}
		else {
			printf("%u\n", n);
		}
	}
	return 0;
}
