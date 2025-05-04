class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]= []
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_g(self):
        for node in self.graph:
            print(f"{node}--> {','.join(map(str,self.graph[node]))}")

g = Graph()
g.add_edge(3,4)
g.add_edge(5,2)
g.add_edge(4,5)
g.add_edge(2,6)
g.print_g()
