	import java.util.Scanner;

	import java.util.Arrays;

	 

	public class Main {

	    public static void main(String[] args) {

	        Scanner sc = new Scanner(System.in);

	        

	        int[] wList = getPointList(sc);

	        int[] kList = getPointList(sc);

	        

	        System.out.println(Arrays.stream(wList).sum() + " " + Arrays.stream(kList).sum());

	    }

	    

	    private static int[] getPointList(Scanner sc) {

	        int[] pointList = new int[10];

	        

	        for (int i = 0; i < 10; i++) {

	            pointList[i] = sc.nextInt();

	        }

	        

	        Arrays.sort(pointList);

	        

	        return new int[] {pointList[7], pointList[8], pointList[9]};

	    }

	}