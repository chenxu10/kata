from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self,u, v):
        self.graph[u].append(v)

    def dfs(self, v, vdegree, visited, k):
        visited.add(v)

        for i in self.graph[v]:
            if vdegree[v] < k:
                vdegree[i] = vdegree[i] - 1
            if i not in visited:
                self.dfs(i, vdegree, visited, k)
 
    def kscore(self,k):
        visited = set()
        degree = defaultdict(lambda:0)

        for i in list(self.graph):
            degree[i] = len(self.graph[i])

        for i in list(self.graph):
            if i not in visited:
                self.dfs(i, degree, visited, k)

        for i in list(self.graph):
            if degree[i] >= k:
                print(str("\n [ ") + str(i) + str(" ]"), end=" ")
 
                for j in self.graph[i]:
                    if degree[j] >= k:
                        print("-> " + str(j), end=" ")
 
                print()

        
def test_kcore_graph():
    graph = Graph()
    graph.add_edge(3,5)
    graph.add_edge(5,3)
    graph.add_edge(5,2)
    graph.add_edge(3,4)
    graph.add_edge(3,2)
    graph.kscore(2)

if __name__ == '__main__':
    test_kcore_graph()