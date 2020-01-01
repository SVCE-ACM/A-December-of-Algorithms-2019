from collections import defaultdict 
   
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = []  
          
   
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
   
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
   
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
   
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
   
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    def KruskalMST(self): 
  
        result =[] 
  
        i = 0  
        e = 0  
  
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
   
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        while e < self.V -1 : 
  
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
   
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y) 
        return result

def minimize_cost(edgelist):
    cities = []
    for edge in edgelist:
        cities += edge[:2]
    cities = list(set(cities))
    g = Graph(len(cities))
    for edge in edgelist:
        edge[0] = cities.index(edge[0])
        edge[1] = cities.index(edge[1])
        g.addEdge(*edge)
    result = g.KruskalMST()   
    total_cost = 0
    for u,v,weight  in result:  
        #print(cities[u], cities[v], weight)
        total_cost += weight
    print(total_cost)    