namespace Solution {
  class Program {
    static void Main(string[] args) {

      var l = int.Parse(Console.ReadLine()!);
      var t = int.Parse(Console.ReadLine()!);

      var diff = 2 * t - l;
      Console.WriteLine(diff);

    }
  }
}
