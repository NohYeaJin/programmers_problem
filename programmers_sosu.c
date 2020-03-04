#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
	int i, j, k;
	int n;
	int answer = 0;
	int num = 0;
	int half = 0;
	for (i = 0; i < (nums_len - 2); i++) {
		for (j = i+1; j < (nums_len - 1); j++) {
			for (k = j+1; k < nums_len; k++) {
				num = nums[k] + nums[i] + nums[j];
				half = num / 2;
				for (n = 2; n < half; n++) {
					if ((num % n) == 0) {
						answer = answer - 1;
						break;
					}
				}
				answer = answer + 1;
			}
		}
	}
	return answer;
}