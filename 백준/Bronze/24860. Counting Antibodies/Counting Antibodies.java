import java.util.Scanner;
import java.math.BigInteger;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		BigInteger vk = sc.nextBigInteger();
		BigInteger jk = sc.nextBigInteger();
		BigInteger vr = sc.nextBigInteger();
		BigInteger jr = sc.nextBigInteger();
		BigInteger vh = sc.nextBigInteger();
		BigInteger dh = sc.nextBigInteger();
		BigInteger jh = sc.nextBigInteger();
		BigInteger c1 = vh.multiply(dh).multiply(jh).multiply(vk).multiply(jk);
		BigInteger c2 = vh.multiply(dh).multiply(jh).multiply(vr).multiply(jr);
		
		System.out.println(c1.add(c2));
		sc.close();
	}
}