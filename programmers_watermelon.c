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
			strcat(answer, "����");
		}
	}
	if (nameoji > 0)
	{
		strcat(answer,"��");
	}
	// ������ ���� �޸𸮸� ���� �Ҵ����ּ���.
	return answer;
}