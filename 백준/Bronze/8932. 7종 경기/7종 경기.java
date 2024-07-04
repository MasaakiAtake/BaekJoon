import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[7];
		
		for(int i = 0; i < N; i++) {
			int sum = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());
			//각배열에 순서대로 입력 값을 저장
			for(int j = 0; j < 7; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
			}
			//나온 공식대로 연산 후 sum변수에 더한다.
			sum += (9.23076) * Math.pow((26.7 - arr[0]), 1.835);
			sum += (1.84523) * Math.pow((arr[1] - 75), 1.348);
			sum += (56.0211) * Math.pow((arr[2] - 1.5), 1.05);
			sum += (4.99087) * Math.pow((42.5 - arr[3]), 1.81);
			sum += (0.188807) * Math.pow((arr[4] - 210), 1.41);
			sum += (15.9803) * Math.pow((arr[5] - 3.8), 1.04);
			sum += (0.11193) * Math.pow((254 - arr[6]), 1.88);
			//출력
			System.out.println(sum);
		}
	}

}