import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(bf.readLine());	
		for(int i=0; i<T; i++) {
			int n = Integer.parseInt(bf.readLine());
			int max = n;
			while(n!=1) {
				n = (n%2 == 0) ? n/2 : (n*3)+1;
				max = Math.max(max, n);
			}
			System.out.println(max);
		}
		bf.close();
	}

}