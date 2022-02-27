using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution
{
    static void Main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        var n = Int32.Parse(Console.ReadLine());
        var board = new List<char[]>();
        for (int i = 0; i < n; i++)
        {
            board.Add(Console.ReadLine().ToCharArray());
        }
        var thisGreaterThanThat = Dictionary<Tuple<int, int>, List<Tuple<int, int>>>();
        var thisLessThanThat = Dictionary<Tuple<int, int>, Tuple<int, int>>();
        int signCount = Int32.Parse(Console.ReadLine());
        for (int i = 0; i < signCount; i++)
        {
            var (y1, x1, y2, x2) = Array.ConvertAll(Console.ReadLine().Split(" "), Int32.Parse);
            thisGreaterThanThat[Tuple(y1, x1)].Add(Tuple(y2, x2));
            thisLessThanThat[Tuple(y2, x2)].Add(Tuple(y1, x1));
        }
        getSpotOptions(board, 0, 0);
    }

    static void getSpotOptions(List<char[]> board, int y, int x)
    {
        var allNums = new HashSet<char>();

        var test = from number in Enumerable.Range('1', '1' + board.Count) select (char)number;
        Console.WriteLine(test);

    }
}