import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int countD = 0;
		int countP = 0;
		String[] w = new String[n];
		int d = 0;
		
		for(int i = 0; i < w.length; i++) {
			w[i] = sc.next();
		}
		
		for(int i = 0; i < w.length; i++) {
			if(w[i].equals("D")) {
				countD++;
			}else if(w[i].equals("P")) {
				countP++;
			}
			
			if(countD > countP) {
				d = countD - countP;
			}else {
				d = countP - countD;
			}
			
			if(d >= 2) {
				break;
			}
		}
		System.out.println(countD + ":" + countP);
		sc.close();
	}
}