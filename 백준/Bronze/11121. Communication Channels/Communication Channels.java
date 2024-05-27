import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        int t = scanner.nextInt();
        
        for(int i = 0; i < t; i++){
            String inputBianry = scanner.next();
            String outputBianry = scanner.next();
            
            if (inputBianry.equals(outputBianry)) {
                System.out.println("OK");
            }
            else{
                System.out.println("ERROR");
            }
        }
    }
}