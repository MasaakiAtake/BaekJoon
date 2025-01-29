#define _CRT_SECURE_NO_WARNINGS 
#include <bits/stdc++.h>
using std::pair;

int cnt = 0; //몇번째 케이스인가
//블럭의 좌,우상태를 정수로나타낸 값
//[0]:좌 [1]:우
//0: 반듯함(1번,2번과같은)
//1: 볼록사각형
//2: 볼록원형
//3: 오목사각형
//4: 오목원형
int preBlock[2]; //이전블럭
//사실 preBlock의 0번, 좌측은 계산상필요가 없음

void input();
pair<int, int> findBlockKey(char b); //현재나무블럭의 좌우상태 정수로 변환
void setPrevBlock(int left, int right); //이전블럭상태를 설정
bool checkBlock(int left, int right); //이전블럭과 현재블럭이 맞물릴수 있는가 확인


void input() {
	while (true) {
		char in[10001]; //입력받은 블럭조합
		int size = 0; //블럭조각 갯수

		scanf("%s", &in);
		if (in[0] == '0') //종료조건
			break;

		for (int i = 0; i < 10001; i++) { //사용된 블럭갯수 파악
			if (in[i] == '\0')
				break;
			size++; 
		}
		cnt++; //몇번째 블럭인가.
		bool possible = true;

		if (in[0] == '1' && in[size-1] == '2') { //블럭조합의 처음과끝이 1번과 2번이어야 정상
			for (int i = 0; i < size; i++) { //블럭조합의 처음부터 끝까지 탐색
				auto keys = findBlockKey(in[i]); //현재블럭의 좌우 상태를 정수로 변환
				if (i == 0) {//첫회에는 이전블럭 세팅만하고 넘어간다.
					setPrevBlock(keys.first, keys.second);
				}
				else { //첫회이후에는 이전블럭과 현재블럭을 비교하여 가능한지 확인
					//checkBlock: 이전과 현재의 블럭이 맞물릴수있는 상태인지 확인
					if (!checkBlock(keys.first, keys.second)) { //false리턴받을시 불가능함을 출력
						printf("%d. NOT\n", cnt);
						possible = false; //불가능하다.
						break;
					}
				}
			}
		}
		else { //블럭조합의 처음과 끝이 비정상인경우 바로종료
			printf("%d. NOT\n", cnt);
			possible = false;
		}
		//위 과정에서 걸러지지않은경우 가능한 조합임을 출력
		if (possible) {
			printf("%d. VALID\n", cnt);
		}
	}


}

//입력받은 나무블럭번호에따라 블럭의 좌, 우 상태를 정수로 리턴
std::pair<int, int> findBlockKey(char b) {
	int res1, res2;
	switch (b) {
	case '1':
		res1 = 0; //반듯
		res2 = 3; //오목사각형
		break;
	case '2':
		res1 = 3; //오목사각형
		res2 = 0; //반듯
		break;
	case '3':
		res1 = 3; //오목사각
		res2 = 3; //오목사각
		break;
	case '4':
		res1 = 1; //볼록사각
		res2 = 1; //볼록사각
		break;
	case '5':
		res1 = 1; //볼록사각
		res2 = 4; //오목원형
		break;
	case '6':
		res1 = 4; //오목원형
		res2 = 1; //볼록사각
		break;
	case '7':
		res1 = 4; //오목원형
		res2 = 4; //오목원형
		break;
	case '8':
		res1 = 2; //볼록원형
		res2 = 2; //볼록원형
		break;
	}

	return { res1, res2 };
}

//이전블럭을 재설정하는 함수
void setPrevBlock(int left, int right) {
	preBlock[0] = left;
	preBlock[1] = right;
}

//현재블럭의 좌우상태를 정수로 전달받아 이전블럭과비교하여 가능한 조합인지 확인
//true : 정상
//false 를 리턴할시 불가능함을 출력하고 종료
bool checkBlock(int left, int right) { //현재블럭의상태 left, right
	int preBlockRight = preBlock[1]; //이전블럭의 오른쪽부분
	int nowBlockLeft = left; //현재블럭의 왼쪽부분
	
	bool possible = false;
	//두개가 맞물릴수있는 경우면 정상이다.
	if ((preBlockRight == 1 && nowBlockLeft == 3) ||
		(preBlockRight == 3 && nowBlockLeft == 1) || 
		(preBlockRight == 2 && nowBlockLeft == 4) || 
		(preBlockRight == 4 && nowBlockLeft == 2))
		possible = true;

	//이전블럭 을 현재블럭상태로 갱신
	setPrevBlock(left, right);

	return possible;
}

int main(void) {
	input();

	return 0;
}