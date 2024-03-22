from collections import defaultdict

class DirectedCycle(object):
    def __init__(self, G, numCourses):
        self._marked = [False for _ in range(numCourses)]
        self._onStack = [False for _ in range(numCourses)]
        self._cycle = []
        self._edgeTo = [None for _ in range(numCourses)]
        self.DirectedCycle(G)
    
    def DirectedCycle(self, G):
        for v in G:
            if not self._marked[v]:
                self._dfs(G,v)

    def hasCycle(self):
        return len(self._cycle) > 0

    def cycle(self):
        return self._cycle 

    def _find_numNodes(self,G):
        temp = []
        
        for key, value in G.items():
            temp.append(key)
            temp.append(value[0])
        
        temp = [i for i in temp if i!=None]
        numNodes = max(temp) + 1
        
        return numNodes

    def _dfs(self, G, v):
        self._onStack[v] = True
        self._marked[v] = True

        for w in G[v]:
            if self.hasCycle():
                return
            elif not self._marked[w]: #1
                self._edgeTo[w] = v
                self._dfs(G, w)
            elif self._onStack[w]:
                x = v
                while x != w:
                    x = self._edgeTo[x]
                    self._cycle.append(x)
                self._cycle.append(w)
                self._cycle.append(v)     
        
        self._onStack[v] = False

# Related problems: leetcode 207
# Follow up questions: Think of two methods to detect if there's a circle

if __name__ == '__main__':
    numCourses = 6
    prerequisites = [[5,3],[4,5],[3,4],[5,0]]
    graph = defaultdict(list)

    for children, parent in prerequisites:
        graph[parent].append(children)
        # graph[children].append(None)
 
    print(graph)
    finder = DirectedCycle(graph, numCourses)
    print(finder.hasCycle())
    print(finder.cycle())
