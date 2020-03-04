#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
	bool answer = false;
	int sum = 0;
	int num = x;
	while (x >= 10) {
		sum = sum + (x % 10);
		x = x / 10;
	}
	sum = sum + x;
	if ((num % sum) == 0) {
		answer = true;
	}	
	return answer;
}
