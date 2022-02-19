INFTY = 9999999999999

def my_argmin(keys,arr):
  small = INFTY
  skey = None
  for key in keys:
    if arr[key] < small:
      skey = key
      small = arr[key]
  return skey



#** Straight up Dijkstra's Algorithmn
def dijkstra(g,dist,src,dest):

  Q = list(g.keys())

  while len(Q) > 0:
    u = my_argmin(Q,dist[src])
    Q.remove(u)

    for v in g[u].keys():
      if v in Q:
        alt = dist[src][u] + g[u][v]
        if alt < dist[src][v]:
          dist[src][v] = alt
  return dist





#** Solution
def sol(graph,src,dest):
  nodes = list(graph.keys()) #* Node List
  sp = {} #* Shortest Paths Dictionary
  for i in range(len(nodes)):
    Fr = nodes[i]
    sp[Fr] = {}
    for j in range(len(nodes)):
      To = nodes[j]
      distance = 0 if i==j else INFTY
      sp[Fr].update({To:distance})

  
  sp = dijkstra(graph,sp,src,dest)
  print(sp[src][dest])


# def main():
Ns,Cs,Qs = list(map(int,input().split()))

g = {}
for _ in range(Cs): 
    F,T,V = input().split()
    V = int(V)

    if g.get(F,None) is None:
      g[F] = {T:V}
    else:
      g[F].update({T:V})

    if g.get(T,None) is None:
      g[T] = {F:V}
    else:
      g[T].update({F:V})

queries = []
for _ in range(Qs): queries.append(input())


for q in queries:
  s,d = q.split()
  sol(g,s,d)




# if __name__ == "__main__":
#   main()