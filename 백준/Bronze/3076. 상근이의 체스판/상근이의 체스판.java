import java.util.Scanner;
 
class Main {
    static int R,C,A,B;
    static char[][] map;
    static StringBuilder sb = new StringBuilder();
    
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        
        R = sc.nextInt();
        C = sc.nextInt();
        A = sc.nextInt();
        B = sc.nextInt();
        
        map = new char[R*A][C*B];
        
        for (int i = 0; i < R*A; i+=A) {
            for (int j = 0; j < C*B; j+=B) {
                char c  = '.';
                if((i/A % 2 == 0 && j/B % 2 == 0) || (i/A % 2 != 0 && j/B % 2 != 0)) {
                    c = 'X';
                }
                
                for (int a = i; a < i+A ; a++) {
                    for (int b = j; b < j+B; b++) {
                        map[a][b] = c;
                    }
                }
            }
        }
        
        for (int i = 0; i < R*A; i++) {
            sb.append(map[i]);
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }
}
