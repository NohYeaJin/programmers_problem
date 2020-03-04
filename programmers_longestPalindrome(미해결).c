#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// �Ķ���ͷ� �־����� ���ڿ��� const�� �־����ϴ�. �����Ϸ��� ���ڿ��� �����ؼ� ����ϼ���.
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