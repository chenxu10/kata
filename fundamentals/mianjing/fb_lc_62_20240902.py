def unique_paths(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

def unique_paths_space_optimized(m, n):
    dp = [1] * n
    for i in range(1,m):
        for j in range(1,n):
            dp[j] += dp[j-1]
    return dp[-1]

class Graph:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.adj_list = {}
        self._build_graph()

    def _build_graph(self):
        for i in range(self.rows):
            for j in range(self.cols):
                node = (i, j)
                self.adj_list[node] = []
                if i < self.rows - 1:
                    self.adj_list[node].append((i+1, j))
                if j < self.cols - 1:
                    self.adj_list[node].append((i, j+1))

    def dfs(self, start, end, path, paths):
        if start == end:
            paths.append(path)
            return
        for neighbor in self.adj_list[start]:
            self.dfs(neighbor, end, path + [neighbor], paths)

def unique_paths_graph(m, n):
    graph = Graph(m, n)
    start = (0, 0)
    end = (m-1, n-1)
    paths = []
    graph.dfs(start, end, [start], paths)
    return len(paths)