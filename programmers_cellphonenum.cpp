#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// �Ķ���ͷ� �־����� ���ڿ��� const�� �־����ϴ�. �����Ϸ��� ���ڿ��� �����ؼ� ����ϼ���.
char* solution(const char* phone_number) {
	// return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
	char* answer;
	answer = (char*)malloc(strlen(phone_number) + 1);
	answer[strlen(phone_number)] = '\0';
	for (int i = 0; i < strlen(phone_number); i++) {
		if (strlen(phone_number) - 5 < i &&  i <= strlen(phone_number) - 1) {

			answer[i] = phone_number[i];
		}
		else {
			answer[i] = '*';
		}
	}

	return answer;
}
int main(void) {
	char set[] = { '0','1','3','4' };
	printf("%s", solution(set));
}
