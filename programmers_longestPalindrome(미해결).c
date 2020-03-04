#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
	int answer = 0;
	int len = strlen(s);
	int i = 0;
	int j = len - 1;
	bool palindrome;
	int palin = 1;
	while (i != j) {
		if (s[j] != s[i]) {
			j = j - 1;
			palindrome = false;
		}
		else {
			j = j - 1;
			i = i + 1;
			palindrome = true;
			palin = palin + 2;
		}
	}
	if (palindrome == true) {
		answer = palin;
	}
	return answer;
}
int main(void) {
	char s[250000];
	scanf("%s", s);
	printf("%d", solution(s));
	return 0;
}