import java.util.Scanner;

public class Main {
	static final int max = 5000;
	static final int max2 = 4000;

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int R = scan.nextInt();	// 빨강
		int B = scan.nextInt();	// 갈색
		int L = 0;
		int W = 0;

		for(int i=1; i<=max; i++) {
			for(int j=1; j<=max2; j++) {
				if(R+B == i*j) {
					if(R == (i*2) + (j-2)*2) {
						L = i;
						W = j;
						break;
					}
					else if(R == (j*2) + (i-2)*2) {
						L = j;
						W = i;
						break;
					}
				}
			}
		}

		System.out.println(L + " " + W);
		scan.close();
	}

}