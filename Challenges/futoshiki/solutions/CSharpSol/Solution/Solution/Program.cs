using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution2
{
    public static char dummy = '#';
    public static Dictionary<Tuple<int, int>, List<Tuple<int, int>>> thisGreaterThanThat;
    public static Dictionary<Tuple<int, int>, List<Tuple<int, int>>> thisLessThanThat;
    public static List<char[]> answer;

    static void Main2()
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        var n = Int32.Parse(Console.ReadLine());
        var board = new List<char[]>();
        for (int i = 0; i < n; i++)
        {
            board.Add(Console.ReadLine().ToCharArray());
        }
        thisGreaterThanThat = new Dictionary<Tuple<int, int>, List<Tuple<int, int>>>();
        thisLessThanThat = new Dictionary<Tuple<int, int>, List<Tuple<int, int>>>();
        int signCount = Int32.Parse(Console.ReadLine());
        for (int i = 0; i < signCount; i++)
        {
            var ints = Array.ConvertAll(Console.ReadLine().Split(), x => Int32.Parse(x));
            var y1 = ints[0];
            var x1 = ints[1];
            var y2 = ints[2];
            var x2 = ints[3];

            var cur1 = Tuple.Create(y1, x1);
            if (!thisGreaterThanThat.ContainsKey(cur1))
                thisGreaterThanThat[cur1] = new List<Tuple<int, int>>();
            thisGreaterThanThat[cur1].Add(Tuple.Create(y2, x2));

            var cur2 = Tuple.Create(y2, x2);
            if (!thisLessThanThat.ContainsKey(cur2))
                thisLessThanThat[cur2] = new List<Tuple<int, int>>();
            thisLessThanThat[cur2].Add(Tuple.Create(y1, x1));
        }
        //getSpotOptions(board, 0, 0);
        solve(board, 0);
        printBoard(answer);
        //foreach (var line in answer)
        //{
        //    Console.WriteLine(new string(line));
        //}
        //Console.WriteLine("done");

    }

    static HashSet<char> getSpotOptions(List<char[]> board, int curY, int curX)
    {
        var allNums = new HashSet<char>();
        for (int i = 0; i < board.Count; i++)
        {
            allNums.Add((char)('1' + i));
        }

        //Console.WriteLine($"all nums {string.Join("", allNums)}");


        for (int x = 0; x < board.Count; x++)
        {
            if (x == curX)
                continue;
            if (board[curY][x] != dummy)
                allNums.Remove(board[curY][x]);
        }

        for (int y = 0; y < board.Count; y++)
        {
            if (y == curY)
                continue;
            if (board[y][curX] != dummy)
                allNums.Remove(board[y][curX]);
        }
        //return allNums

        var curSpot = Tuple.Create(curY, curX);

        if (thisGreaterThanThat.ContainsKey(curSpot))
        {
            foreach (var other in thisGreaterThanThat[curSpot])
            {
                var otherY = other.Item1;
                var otherX = other.Item2;
                if (board[otherY][otherX] == dummy)
                {
                    var toRemove = (char)('0' + 1);
                    allNums.Remove(toRemove);
                    continue;
                }
                for (int i = 1; i < board[otherY][otherX] - '0' + 1; i++)
                {
                    var toRemove = (char)('0' + i);
                    //Console.WriteLine($"greater to remove {toRemove}");
                    allNums.Remove(toRemove);
                }
            }
        }

        if (thisLessThanThat.ContainsKey(curSpot))
        {
            foreach (var other in thisLessThanThat[curSpot])
            {
                var otherY = other.Item1;
                var otherX = other.Item2;
                if (board[otherY][otherX] == dummy)
                {
                    var toRemove = (char)('0' + board.Count);
                    allNums.Remove(toRemove);
                    continue;
                }
                for (int i = board[otherY][otherX] - '0'; i < board.Count + 1; i++)
                {
                    var toRemove = (char)('0' + i);
                    //Console.WriteLine($"less to remove {toRemove}");
                    allNums.Remove(toRemove);
                }
            }
        }


        return allNums;
        //var test = from number in Enumerable.Range('1', '1' + board.Count) select (char)number;
        //Console.WriteLine(test);

    }

    static void printBoard(List<char[]> board)
    {
        foreach (var line in board)
        {
            Console.WriteLine(new string(line));
        }
    }

    static bool solve(List<char[]> board, int pos)
    {
        //Console.WriteLine($"pos {pos}");

        if (pos == board.Count * board.Count)
        {
            answer = board;
            return true;
        }
        int curY = pos / board.Count;
        int curX = pos % board.Count;
        if (board[curY][curX] != dummy)
            return solve(board, pos + 1);
        var options = getSpotOptions(board, curY, curX);
        //Console.WriteLine($"pos {curY} {curX}");
        //Console.Write("options: ");
        //Console.WriteLine(string.Join(" ", options));

        //printBoard(board);
        if (options.Count == 0)
            return false;
        foreach (var option in options)
        {
            List<char[]> current = new List<char[]>(board.Count);

            board.ForEach((item) =>
            {
                current.Add((char[])item.Clone());
            });
            current[curY][curX] = option;
            if (columnHasValids(current, curY, curX) == false || rowHasValids(current, curX, curY) == false)
                continue;
            bool works = solve(current, pos + 1);

            //purposely removed to test against the worst case instead of stopping early

            //if (works)
            //return true;
        }
        return false;

    }

    static bool columnHasValids(List<char[]> board, int startY, int curX)
    {
        for (int y = startY; y < board.Count; y++)
        {
            if (getSpotOptions(board, y, curX).Count == 0)
                return false;
        }

        return true;
    }
    static bool rowHasValids(List<char[]> board, int startX, int curY)
    {
        for (int x = startX; x < board.Count; x++)
        {
            if (getSpotOptions(board, curY, x).Count == 0)
                return false;
        }

        return true;
    }
}