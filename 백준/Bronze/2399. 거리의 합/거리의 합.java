import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int [] x = new int [N];
        long allDistance = 0;
        
        for(int i=0; i<N; i++)
                x[i] = sc.nextInt();
                
        for(int i=0; i<x.length; i++)
                for(int j=0; j<x.length; j++)
                        allDistance += Math.abs(x[i]-x[j]);
                        
        System.out.println(allDistance);
        sc.close();
    }
}