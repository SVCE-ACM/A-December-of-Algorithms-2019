def minDistance(dist, sptSet, n): 
	mini = 10000
	min_index = -1
	for v in range(n): 
		if(dist[v] < mini and sptSet[v] == False): 
			mini = dist[v] 
			min_index = v 
	return min_index 

def minimize_cost(src,graph,n): 
	tot = 0
	dist = [10000] * n 
	dist[src] = 0
	sptSet = [False] * n 
	parent = [-1] * n
	for cout in range(n): 
		u = minDistance(dist, sptSet,n) 
		sptSet[u] = True
		for v in range(n): 
			if (graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]): 
				dist[v] = dist[u] + graph[u][v] 
				parent[v] = u
	for i in range(len(parent)):
		if(parent[i] >= 0):
			tot += graph[parent[i]][i]
	return tot 

n = int(input('How many edges:'))
edge = []
vertex = set()
for i in range(n):
    edge.append(input('Edge {}:'.format(i+1)).split())
    edge[i][2] = int(edge[i][2])
    vertex.add(edge[i][0])
    vertex.add(edge[i][1])
V = dict()
i =  s = 0
for e in vertex:
    if(e == 'S' or e == 's'):
        s = i
    V[e] = i
    i += 1
graph = []
for _ in range(n):
    graph.append([0 for _ in range(n)])
for e in edge:
    graph[V[e[0]]][V[e[1]]] = e[2]

print('Minimum cost: ',minimize_cost(s,graph,n))