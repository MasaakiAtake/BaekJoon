import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 핸드폰에 연결한 횟수
        int useB = 0; // 소모한 배터리
        int nowB = 0; // 현재 배터리 소모량
        int phoneNum = 0; // 연결된 휴대폰 번호

        int[] phoneArr = new int[N]; 
        
        for(int i=0; i<N; i++){
            phoneArr[i] = sc.nextInt();

            if(phoneNum == phoneArr[i]){ // 이미 연결된 휴대폰에 재연결하는 경우
                useB = useB*2;
                nowB = nowB + useB;
            } else { // 새로운 휴대폰에 연결하는 경우
                phoneNum = phoneArr[i];
                useB = 2;
                nowB = nowB + useB;
            }
            if(nowB >= 100){ // 누적 배터리 소모량이 100퍼 이상인 경우
                phoneNum = 0;
                useB = 0;
                nowB = 0;
            }
        }
        System.out.println(nowB);
    sc.close();
    }
}
