from collections import defaultdict as dd, deque
import heapq
total_places, streets, queries = map(int, input().split())

    
dists = dd(lambda: dd(lambda : float("inf")))
for _ in range(streets):
    from_, to, dist = input().split()
    dist = int(dist)
    dists[from_][to] = min(dist, dists[from_][to])
    dists[to][from_] = min(dist, dists[to][from_])




def djikstra(start, goal):
    DJIK = False
    if DJIK:
        fringe = []
        heapq.heapify(fringe)
    else:
        fringe = []
    # for j, start in enumerate(dists):
    # print(j)
    if DJIK:
        heapq.heappush(fringe, (0, start))
    else:
        fringe.append((0, start))
    # print("start", start)
    seen = set()
    # cur_graph = dd(lambda : float("inf"))
    while len(fringe):
        cost, cur = heapq.heappop(fringe) if DJIK else min(fringe)
        fringe.remove((cost, cur))
        # print(cur)
        if cur in seen:
            continue
        seen.add(cur)
        # if cur == goal:
            # return cost
        if dists[start][cur] > cost:
            dists[start][cur] = cost
        # else:
            # continue

        for other in dists[cur]:
            if other in seen:
                continue
            new = (cost + dists[cur][other], other)
            if DJIK:
                heapq.heappush(fringe, new)
            else:
                fringe.append(new)

    # dists[start] = cur_graph
    # print(dists)

    # for n in needed_list:
        # from_, to = n
        # print(dists[from_][to])

# needed_list = []
# needed_spots = {}
# single_needed = set()
for _ in range(queries):
    from_, to = input().split()
    if to not in dists[from_]:
        djikstra(from_, to)
    print(dists[from_][to])

    # needed_spots[from_] = to
    # needed_spots[to] = from_
    # needed_list.append((from_, to))
# print(dists)
# for x in dists:
    # print(x, dists[x])


    # print(dists[from_][to])