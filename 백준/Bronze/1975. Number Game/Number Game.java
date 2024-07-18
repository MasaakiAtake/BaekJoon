import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		//0의 갯수를 셀 숫자의 갯수 T만큼 반복
		for(int i = 0; i < T; i++) {
			//0의 갯수를 저장할 변수
			int count = 0;
			int N = Integer.parseInt(br.readLine());
			//N의 진수들을 계산하는 거기에 N까지만 반복
			for(int j = 2; j <= N; j++) {
				//변해도 상관없는 변수에 N값을 저장
				int val = N;
				//해당 진수의 숫자마다 반복 횟수가 달라지기 때문에 무한 루프
				while(true) {
					//val을 j로 나눠서 나머지가 0이 아니면 무한루프 종료
					if(val % j != 0) {
						break;
					}
					count++;
					val /= j;
				}
			}
			System.out.println(count);
		}
	}
}