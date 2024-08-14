import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String S = br.readLine();
		//O가 공의 위치.
		ArrayList<String> list = new ArrayList<String>(Arrays.asList("O", "X", "X"));
		
		//문자열의 길이만큼 반복하는 반복문
		for(int i = 0; i < S.length(); i++) {
			if(S.charAt(i) == 'A') {
				//collections.swap은 입력된 list의 두 인덱스 값의 위치를 바꿔주는 함수
				Collections.swap(list, 0, 1);
			}else if(S.charAt(i) == 'B') {
				Collections.swap(list, 1, 2);
			}else if(S.charAt(i) == 'C') {
				Collections.swap(list, 0, 2);
			}
		}
		
		System.out.println(list.indexOf("O") + 1);
	}

}