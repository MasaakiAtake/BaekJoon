import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[] resultArr = new int[5];

        char[][] map = new char[(5 * M) + 1][(5 * N) + 1];
        for (int i = 0; i < (5 * M) + 1; i++) {
            String s = br.readLine();
            for (int j = 0; j < (5 * N) + 1; j++) {
                map[i][j] = s.charAt(j);
            }
        }

        int idx_x = 1;
        while (M-- > 0) {
            int idx_y = 1;
            for (int i = 0; i < N; i++) {
                int starCnt = 0;
                for (int j = idx_x; j < idx_x + 4; j++) {
                    for (int k = idx_y; k < idx_y + 4; k++) {
                        if (map[j][k] == '*') {
                            starCnt += 1;
                        }
                    }
                }

                resultArr[starCnt / 4] += 1;
                idx_y += 5;
            }
            idx_x += 5;
        }

        for (int i = 0; i < resultArr.length; i++) {
            bw.write(Integer.toString(resultArr[i]) + " ");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}