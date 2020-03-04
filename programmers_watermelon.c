#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(int n) {
	char* answer = (char*)malloc(sizeof(char)*(n * 500));
	int mok = n / 2;
	int nameoji = n % 2;
	int i = 0;
	if (mok >= 1) 
	{
		for (i = 0; i < mok; i++) 
		{
			strcat(answer, "수박");
		}
	}
	if (nameoji > 0)
	{
		strcat(answer,"수");
	}
	// 리턴할 값은 메모리를 동적 할당해주세요.
	return answer;
}