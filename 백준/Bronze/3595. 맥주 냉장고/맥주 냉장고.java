import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = read(), a = 0, b = 0, c = 0, min = Integer.MAX_VALUE;
        for (int i = 1; i * i * i <= n; i++) {
            if (n % i == 0) {
                for (int j = i; j * j <= n / i; j++) {
                    if (n / i % j == 0) {
                        int k = n / i / j, val = i * j + j * k + i * k;
                        if (min > val) {
                            min = val;
                            a = i;
                            b = j;
                            c = k;
                        }
                    }
                }
            }
        }

        bw.write(a + " " + b + " " + c);
        bw.flush();
    }

    private static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);

        return n;
    }

}