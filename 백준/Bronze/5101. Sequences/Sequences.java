import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true) {
            int firstNum = sc.nextInt();
            int gap = sc.nextInt();
            int testNum = sc.nextInt();

            if (firstNum == 0 && gap == 0 && testNum == 0) break;
            else if ((testNum - firstNum) % gap != 0 || testNum < firstNum)
                System.out.println("X");
            else
                System.out.println(((testNum - firstNum) / gap) + 1);
        }
    }
}