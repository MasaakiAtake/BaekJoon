namespace Solution {
  class Program {
    static void Main(string[] args) {

      while (true) {
        var input = Console.ReadLine()?.Split(' ');
        if (input == null) break ;

        var n = int.Parse(input[0]);
        var w = int.Parse(input[1]);
        var d = int.Parse(input[2]);
        var totalWeight = int.Parse(input[3]);

        var standardWeight = w * ((n - 1) * n) / 2;
        var numBasket = (standardWeight - totalWeight) / d;

        if (numBasket == 0) Console.WriteLine(n);
        else Console.WriteLine(numBasket);
      }

    }
  }
}