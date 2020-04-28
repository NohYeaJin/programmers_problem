#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
	int answer = 0;
	int fibo[100000];
	fibo[0] = 0;
	fibo[1] = 1;
	for (int i = 2; i <= n; i++) {
		fibo[i] = fibo[i - 1] + fibo[i - 2];
	}
	return fibo[n] % 1234567;
}
int main(void) {
	
	printf("%d", solution(9999));
}
