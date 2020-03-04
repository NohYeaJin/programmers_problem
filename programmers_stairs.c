#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int n) {
	if (n == 1||n==0) {
		return 1;
	}
	else
		return solution(n - 1) + solution(n - 2);
}

int main(void) {
	int n;
	int result;
	scanf("%d", &n);
	result = solution(n);
	printf("%d", result);
}