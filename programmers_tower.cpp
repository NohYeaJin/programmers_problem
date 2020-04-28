#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int seekseek(int stack[], int num, int height) {
	for (int j = num - 1; j >= 0; j--) {
		if (stack[j] > height) {
			return j+1;
		}
	}
	return 0;
}
// heights_len은 배열 heights의 길이입니다.
int* solution(int heights[], size_t heights_len) {
	// return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
	int* stack = (int*)malloc(sizeof(stack)*heights_len);
	int* answer = (int*)malloc(sizeof(answer)*heights_len);
	int height;
	for (int i = 0; i < heights_len; i++) {
		stack[i] = heights[i];
		height = heights[i];
		answer[i]=seekseek(stack, i, height);
	}
	for (int i = 0; i < heights_len; i++) {
		printf("%d", answer[i]);
	}
	return answer;
}

int main(void) {

	int heights[] = {6,9,5,7,4};
	solution(heights, 5);

}