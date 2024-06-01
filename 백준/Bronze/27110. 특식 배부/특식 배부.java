import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main extends Exception {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int chicken = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int Fried = Integer.parseInt(st.nextToken());
        int Ganjang = Integer.parseInt(st.nextToken());
        int yang = Integer.parseInt(st.nextToken());

        int answer = 0;

        if (Fried >= chicken){
            Fried = chicken;
        }else{
            Fried = Fried;
        }

        if (Ganjang >= chicken){
            Ganjang = chicken;
        }else{
            Ganjang = Ganjang;
        }

        if (yang >= chicken){
            yang = chicken;
        }else{
            yang = yang;
        }

        answer = Fried + Ganjang + yang;
        sb.append(answer);

        System.out.println(sb.toString());
    }
}