from collections import defaultdict as dd, deque
import heapq
total_places, streets, queries = map(int, input().split())

    
dists = dd(lambda: dd(lambda : float("inf")))
for _ in range(streets):
    from_, to, dist = input().split()
    dist = int(dist)
    dists[from_][to] = min(dist, dists[from_][to])
    dists[to][from_] = min(dist, dists[to][from_])

needed_list = []
needed_spots = {}
single_needed = set()
for q in range(queries):
    from_, to = input().split()
    needed_spots[from_] = to
    needed_spots[to] = from_
    needed_list.append((from_, to))


DJIK = True
if DJIK:
    fringe = []
    heapq.heapify(fringe)
else:
    fringe = deque([])
for start in dists:
    if start not in needed_spots:
        continue
    if DJIK:
        heapq.heappush(fringe, (0, start))
    else:
        fringe.append((0, start))
    # print("start", start)
    seen = set()
    while len(fringe):
        if DJIK:
            cost, cur = heapq.heappop(fringe)
        else:
            cost, cur = fringe.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        if dists[start][cur] > cost:
            dists[start][cur] = cost
            dists[cur][start] = cost

        # print(f"{cur} ----")
        for other in dists[cur]:
            if other == cur:
                continue
            new = (cost + dists[cur][other], other)
            if DJIK:
                heapq.heappush(fringe, (cost + dists[cur][other], other))
            else:
                fringe.append(new)
            # print(other)
        # print(len(fringe))
for n in needed_list:
    from_, to = n
    print(dists[from_][to])
    
# print(dists)
# for x in dists:
    # print(x, dists[x])


    # print(dists[from_][to])