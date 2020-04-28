#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* phone_number) {
	// return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
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
