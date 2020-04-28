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
// heights_len�� �迭 heights�� �����Դϴ�.
int* solution(int heights[], size_t heights_len) {
	// return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
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