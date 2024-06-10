import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main extends Exception {
    public static void main(String[] args) throws IOException {

        // N개의 문제 후보, M개의 찬반 의견
        // M은 항상 홀수이며, 과반수를 넘어야 출제된다.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int answer = 0;

        for (int i = 0; i < N; i++) {
            String opinion = br.readLine();
            int count = 0;

            for (int j = 0; j < M; j++) {
                char oneOpinion = opinion.charAt(j);

                if (oneOpinion == 'O') {
                    count++;
                }
            }
            if (count > (M / 2)) {
                answer++;
            }
        }
        sb.append(answer).append("\n");
        System.out.println(sb.toString());
    }
}