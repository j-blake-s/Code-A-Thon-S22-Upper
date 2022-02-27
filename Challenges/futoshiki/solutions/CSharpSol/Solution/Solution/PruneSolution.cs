
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution
{
    public static char dummy = '#';
    public static Dictionary<Tuple<int, int>, List<Tuple<int, int>>> thisGreaterThanThat;
    public static Dictionary<Tuple<int, int>, List<Tuple<int, int>>> thisLessThanThat;
    public static List<List<HashSet<int>>> answer;

    static void Main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        var n = Int32.Parse(Console.ReadLine());
        var board = new List<List<HashSet<int>>>();
        var allNums = new HashSet<int>();
        for (int i = 1; i < n + 1; i++)
        {
            allNums.Add(i);
        }

        var pruneAfter = new List<Tuple<int, int>>();
        for (int y = 0; y < n; y++)
        {
            var cur = Console.ReadLine();
            board.Add(new List<HashSet<int>>());
            int x = 0;
            foreach (var ch in cur)
            {
                if (ch == dummy)
                {
                    board[board.Count - 1].Add(new HashSet<int>(allNums));
                }
                else
                {
                    var temp = new int[]
                    {
                        ch - '0'
                    };
                    board[board.Count - 1].Add(new HashSet<int>(temp));
                    pruneAfter.Add(new Tuple<int, int>(y, x));
                }
                x += 1;
            }
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
            //pruneAfter.Add(cur1);

            if (!thisGreaterThanThat.ContainsKey(cur1))
                thisGreaterThanThat[cur1] = new List<Tuple<int, int>>();
            thisGreaterThanThat[cur1].Add(Tuple.Create(y2, x2));
            board[y1][x1].Remove(1);

            var cur2 = Tuple.Create(y2, x2);
            //pruneAfter.Add(cur2);
            if (!thisLessThanThat.ContainsKey(cur2))
                thisLessThanThat[cur2] = new List<Tuple<int, int>>();
            thisLessThanThat[cur2].Add(Tuple.Create(y1, x1));
            board[y2][x2].Remove(n);
        }

        foreach (var item in pruneAfter)
        {
            okAfterPruningSpots(ref board, item.Item1, item.Item2);
        }

        //getSpotOptions(board, 0, 0);
        solve(board, 0);
        //Console.WriteLine("answer:");
        printBoard(answer);


    }

    static bool okAfterPruningSpots(ref List<List<HashSet<int>>> board, int curY, int curX)
    {
        //remove row conflicts
        for (int x = 0; x < board.Count; x++)
        {
            if (x == curX)
                continue;
            board[curY][x].Remove(board[curY][curX].ElementAt(0));
            if (board[curY][x].Count == 0)
            {
                //Console.WriteLine($"{curY} {x} none remaining 1");
                return false;
            }
        }

        //remove column conflicts
        for (int y = 0; y < board.Count; y++)
        {
            if (y == curY)
                continue;

            board[y][curX].Remove(board[curY][curX].ElementAt(0));
            if (board[y][curX].Count == 0)
            {
                //Console.WriteLine("none remaining 2");
                return false;
            }
        }

        var curSpot = Tuple.Create(curY, curX);

        if (thisGreaterThanThat.ContainsKey(curSpot))
        {
            foreach (var other in thisGreaterThanThat[curSpot])
            {
                var otherY = other.Item1;
                var otherX = other.Item2;

                for (int i = board[curY][curX].ElementAt(0); i < board.Count + 1; i++)
                {
                    board[otherY][otherX].Remove(i);
                }
                if (board[otherY][otherX].Count == 0)
                {
                    return false;
                }
            }
        }

        if (thisLessThanThat.ContainsKey(curSpot))
        {
            foreach (var other in thisLessThanThat[curSpot])
            {
                var otherY = other.Item1;
                var otherX = other.Item2;
                for (int i = 1; i < board[curY][curX].ElementAt(0) + 1; i++)
                {
                    board[otherY][otherX].Remove(i);
                }
                if (board[otherY][otherX].Count == 0)
                {
                    return false;
                }
            }
        }

        return true;
    }

    static void printBoard(List<List<HashSet<int>>> board)
    {
        for (int y = 0; y < board.Count; y++)
        {
            for (int x = 0; x < board.Count; x++)
            {
                //Console.Write($"({string.Join(" ", board[y][x])})");
                Console.Write($"{board[y][x].ElementAt(0)}");
            }
            Console.WriteLine();
        }

    }

    static bool solve(List<List<HashSet<int>>> board, int pos)
    {
        if (pos == board.Count * board.Count)
        {
            answer = board;
            return true;
        }
        int curY = pos / board.Count;
        int curX = pos % board.Count;

        var options = board[curY][curX];

        if (board[curY][curX].Count == 0)
        {
            return false;
        }

        foreach (var option in options)
        {
            List<List<HashSet<int>>> current = new List<List<HashSet<int>>>();

            board.ForEach((item) =>
            {
                current.Add(new List<HashSet<int>>());
                item.ForEach((cell) =>
                {
                    current[current.Count - 1].Add(new HashSet<int>(cell));
                });
            });
            current[curY][curX] = new HashSet<int>(new int[] { option });

            bool works = okAfterPruningSpots(ref current, curY, curX);
            //Console.WriteLine("after pruning:");
            //printBoard(current);
            if (!works)
                continue;
            works = solve(current, pos + 1);


            if (works)
                return true;
        }
        return false;
    }
}
