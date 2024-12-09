import java.util.*;

public class Main {

	public static class Point {
		public int x, y;
		
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
		
		public int dotNumber() {
			if(x == 1 && y == 1) return 1;
			
			int tx = 1, ty = 1;
			int number = 1;
			
			do {
				if(ty == 1) {
					int t = tx;
					tx = ty;
					ty = t;
					ty++;
				} else {
					tx++;
					ty--;
				}
				number++;
				
				if(tx == x && ty == y) return number;
			} while(true);
		}
		
		public static Point toPoint(int dotNumber) {
			if(dotNumber == 1) return new Point(1, 1);
			
			int tx = 1, ty = 1;
			int number = 1;
			
			do {
				if(ty == 1) {
					int t = tx;
					tx = ty;
					ty = t;
					ty++;
				} else {
					tx++;
					ty--;
				}
				number++;
				
				if(number == dotNumber) return new Point(tx, ty);
			} while(true);
		}
	}
	
	
	public static class Pair {
		public int first;
		public int second;
		
		public Pair(int first, int second) {
			this.first = first;
			this.second = second;
		}
	}
	
	private static List<Pair> data;
	
	private static boolean input() {
		boolean state;
		
		try(Scanner kb = new Scanner(System.in)) {
			data = new ArrayList<>();
			
			int t = kb.nextInt();
			
			for(int i = 0; i < t; i++) {
				int first = kb.nextInt();
				int second = kb.nextInt();
				
				data.add(new Pair(first, second));
			}
			state = true;
		} catch(Exception e) {
			state = false;
		}
		
		return state;
	}
	
	private static void printAnswer() {
		for(Pair p : data) {
			Point p1 = Point.toPoint(p.first);
			Point p2 = Point.toPoint(p.second);
			
			Point p3 = new Point(p1.x + p2.x, p1.y + p2.y);
			
			System.out.println(p3.dotNumber());
		}
	}
	
	public static void main(String[] args) {
		
		if(input()) {
			printAnswer();
		}

	}

}