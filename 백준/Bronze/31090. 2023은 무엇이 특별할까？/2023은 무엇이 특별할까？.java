import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main extends Exception {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int num = Integer.parseInt(br.readLine());
        String answer = "";

        for (int i = 0; i < num; i++) {
            int year = Integer.parseInt(br.readLine());
            int yearTwo = (year % 100);

            if (yearTwo == 0) {
                answer = "Bye";
            } else if ((year + 1) % yearTwo == 0) {
                answer = "Good";
            } else {
                answer = "Bye";
            }

            sb.append(answer).append("\n");
        }

        System.out.println(sb.toString());
    }
}