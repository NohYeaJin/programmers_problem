#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


int solution(int n) {
	int answer = 0;
	while (n >= 10) {
		answer = answer + (n % 10);
		n = n / 10;
	}
	answer = answer + n;
	return answer;
}

int main(void) {
	int n;
	scanf("%d", &n);
	int answer = solution(n);
	printf("%d", answer);
}