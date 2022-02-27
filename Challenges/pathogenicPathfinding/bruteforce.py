INFTY = 9999999999999




def depth(g,cur,dest,dist,visited):
  global min_dist
  if cur == dest:
    min_dist = min(min_dist,dist)
    return 
  else:

    for e in g.get(cur,{}).keys():
      if e not in visited:
        visited.append(e)
        depth(g,e,dest,dist+g[cur][e],visited)
        visited.remove(e)


def sol(g,src,dest):
  global min_dist
  min_dist = INFTY
  depth(g,src,dest,0,[])
  print(min_dist)



min_dist = INFTY
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
  f,t = q.split()
  sol(g,f,t)