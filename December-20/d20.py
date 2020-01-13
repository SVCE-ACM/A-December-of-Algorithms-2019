def TSP(graph, s, V): 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 
	minp = 1000000000
	while True: 
		curp = 0
		k = s 
		for i in range(len(vertex)): 
			curp += graph[k][vertex[i]] 
			k = vertex[i] 
		curp += graph[k][s] 
		minp = min(minp, curp) 
		if not next(vertex): 
			break
	return minp 
def next(L): 
	n = len(L) 
	i = n - 2
	while i >= 0 and L[i] >= L[i + 1]: 
		i -= 1
	if i == -1: 
		return False
	j = i + 1
	while j < n and L[j] > L[i]: 
		j += 1
	j -= 1
	L[i], L[j] = L[j], L[i] 
	left = i + 1
	right = n - 1
	while left < right: 
		L[left], L[right] = L[right], L[left] 
		left += 1
		right -= 1
	return True

V = int(input('Enter no of vertex:'))
graph = []
print('Enter the distance between each city in matrix form')
for _ in range(V):
    row = [int(e) for e in input().split()][0:V]
    graph.append(row)

print('Shortest distance: ',TSP(graph,0,V),'km') 

