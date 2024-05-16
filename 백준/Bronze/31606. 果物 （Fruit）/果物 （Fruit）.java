import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int c = 3;
        int first = scanner.nextInt();
        int second = scanner.nextInt();
        int sum = first + second + c;
        System.out.println(sum);
    }
}