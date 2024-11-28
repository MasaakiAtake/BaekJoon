import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = read(), m = read(), min = Math.min(n, m), max = Math.max(n, m), t = read(), i = 0, b = 0, c = 10000;
        do {
            int sub = t - max * i, tb = sub / min + i, tc = sub % min;

            if (tc < c || tb > b) {
                b = tb;
                c = tc;
            }
        } while (max * ++i <= t);

        bw.write(b + " " + c);
        bw.flush();
    }

    private static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);

        return n;
    }

}