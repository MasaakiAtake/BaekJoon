import java.util.Scanner;

//2804번 
public class Main {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String a=sc.next();
		String b=sc.next();
		int n=0,m=0;
		for (int i = 0; i < a.length(); i++) {
			if(b.indexOf(a.charAt(i))!=-1) {
				n=i;
				m=b.indexOf(a.charAt(i));
				break;
			}
		}
		
		char[][] map=new char[b.length()][a.length()];
		
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				if(i==m) {
					map[i][j]=a.charAt(j);
				}else if(j==n) {
					map[i][j]=b.charAt(i);
				}else {
					map[i][j]='.';
				}
			}
		}
		
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				System.out.print(map[i][j]);
			}
			System.out.println();
		}
		
		
	}
}