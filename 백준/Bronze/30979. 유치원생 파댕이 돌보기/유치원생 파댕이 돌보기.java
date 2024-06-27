import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();
        int n = sc.nextInt();
        int total = 0;
        
        for(int i = 0; i < n; i++){
            int f = sc.nextInt();
            total += f;
        }
        
        if(total >= t){
            System.out.println("Padaeng_i Happy");
        }else{
            System.out.println("Padaeng_i Cry");
        }
        sc.close();
    }
}