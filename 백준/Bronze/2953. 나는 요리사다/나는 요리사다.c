#include <stdio.h>
 
int main() {
 
    int n;            // 점수 입력
    int max = 0;     // 최댓값 찾기
    int maxarr = 0;  // 최댓값 방 찾기

    // for문 밖에 sum을 선언할 경우 5명의 점수가 다 합쳐서 나온다.

    for (int i = 0; i < 5; i++) {

    int sum = 0;    // 5명의 점수가 나온다.

        for (int j = 0; j < 4; j++) {

            scanf("%d", &n);

            sum += n;

            if (sum > max) {
                max = sum;
                maxarr = i + 1; //0번방 부터 시작하기 때문에 1을 더해준다.
            }
        }
    }
        printf("%d %d", maxarr,max);
}