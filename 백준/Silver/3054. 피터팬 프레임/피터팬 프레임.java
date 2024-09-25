import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String str = scan.next();
		String[] sArr = new String[5];
		
		/* 첫번째와 다섯번째 기호 */
		sArr[0] = "..#..";
		sArr[4] = "..#..";
		for(int i=1; i<str.length(); i++) {
			if(i%3 == 2) {	// 3의 배수 웬디 프레임('*') 들어가는 곳
				sArr[0] += ".*..";
				sArr[4] += ".*..";
			}	
			else {	// 피터팬 프레임('#') 들어가는 곳
				sArr[0] += ".#..";
				sArr[4] += ".#..";
			}
		}
		
		/* 두번째와 네번째 기호 */
		sArr[1] = ".#.#.";
		sArr[3] = ".#.#.";
		for(int i=1; i<str.length(); i++) {
			if(i%3 == 2) {	// 3의 배수 웬디 프레임('*') 들어가는 곳
				sArr[1] += "*.*.";
				sArr[3] += "*.*.";
			}
			else {
				sArr[1] += "#.#.";
				sArr[3] += "#.#.";
			}
		}
		
		/* 세번째(중간) 기호 */
		sArr[2] = "#." + str.charAt(0) + ".#";
		for(int i=1; i<str.length(); i++) {
			if(i%3 == 1) {	// 3의 배수 앞에 오는 문자
				sArr[2] += "." + str.charAt(i);
				
				/*
				 * 문자열의 길이가 3, 5일때를 생각해보면
				 * DOG -> 예제와 같이 O에서 끝날때 ".*" 가 붙어야함.
				 * DOGDO -> 마지막에 끝날때 3의 배수위치가 아니므로 ".#" 로 끝나야함.
				 */
				if(i == str.length()-1) 
					sArr[2] += ".#";
				else 
					sArr[2] += ".*";
			}
			else if(i%3 == 2) {	// 가장 마지막 문자(3의 배수 위치)
				sArr[2] += "." + str.charAt(i) + ".*";
			}
			else {	// 가장 첫번째 문자
				sArr[2] += "." + str.charAt(i) + ".#"; 
			}
		}
		
		for(int i=0; i<sArr.length; i++) {
			System.out.println(sArr[i]);
		}
		
		scan.close();
	}

}
