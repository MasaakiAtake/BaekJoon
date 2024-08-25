	import java.util.Scanner;

	 

	public class Main {

	    

	    public static void main(String args[]) {

	        Scanner sc = new Scanner(System.in);

	        

	        while(true) {

	            String bitString = sc.next();

	            

	            // '#' 입력 시 프로그램 종료

	            if (bitString.equals("#")) break;

	            

	            // 수정할 마지막 비트 찾기

	            char correctedBit = correctLastBit(bitString);

	            

	            // 마지막 비트를 올바르게 수정하여 출력

	            System.out.println(bitString.substring(0, bitString.length() - 1) + correctedBit);

	        }

	    }

	    

	    // 마지막 비트를 올바르게 수정하는 함수

	    static char correctLastBit(String bitString) {

	        // 마지막 비트의 패리티 가져오기

	        char parity = bitString.charAt(bitString.length() - 1);

	        

	        // 비트 스트링에서 1의 개수 계산

	        int countOnes = countOnes(bitString);

	        

	        // 현재 패리티와 1의 개수를 비교하여 마지막 비트를 결정

	        if ((countOnes % 2 == 0 && parity == 'e') || (countOnes % 2 == 1 && parity == 'o')) {

	            // 1의 개수와 패리티가 일치하면 마지막 비트를 0으로 설정

	            return '0';

	        } else {

	            // 1의 개수와 패리티가 일치하지 않으면 마지막 비트를 1로 설정

	            return '1';

	        }

	    }

	    

	    // 비트 스트링에서 1의 개수를 세는 함수

	    static int countOnes(String bitString) {

	        int count = 0;

	        

	        // 마지막 비트를 제외하고 순회 하여 1의 개수 카운트

	        for (int i = 0; i < bitString.length() - 1; i++) {

	            if (bitString.charAt(i) == '1') {

	                count++;

	            }

	        }

	        

	        return count;

	    }

	    

	}