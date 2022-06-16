import re
import collections as cx

def adjtxtblk2OrderedDict(txtblk):
  """Convert a text-block representing an adjacency list into an array."""
  lst = []
  for line in txtblk.splitlines():
    line = line.strip()
    if line:
      lst.append(_adjstr2arr(line))
  return cx.OrderedDict(lst)

def _adjstr2arr(adjstr):
  """Convert "A:  F B E" to ('A', ('F', 'B', 'E'))."""
  M = re.search(r'^(\S+)\s*:\s*(\S.*)$', adjstr)
  if M:
    return (M.group(1), M.group(2).split())

class UndirectedGraph():
    def __init__(self, arg=None, **kwargs):
        if arg is not None:
            if isinstance(arg, int):
                self._init_empty(arg)
            elif len(arg) == 1:
                self._init_empty(arg[0])
            else:
                self._init(arg)
            self.keys = range(self.num_nodes)
        elif 'adjtxt' in kwargs:
            self._adj = adjtxtblk2OrderedDict(kwargs['adjtxt'])
            self.num_nodes = len(self._adj)
            self.num_edges = self._init_num_edges()
            self.keys = self._adj.keys()

    def addEdge(self, node_v, node_w):
        """Adds the undirected edge node_v-node_w to self graph."""
        self.add_edge(node_v, node_w)

    def add_edge(self, node_v, node_w):
        """Adds the undirected edge node_v-node_w to self graph."""
        #self._validateVertex(node_v)
        #self._validateVertex(node_w)
        self.num_edges += 1
        self._adj[node_v].add(node_w)
        self._adj[node_w].add(node_v)

    def _init_empty(self, num_nodes):
        """
        Init an empty graph with N vertices
        """
        if num_nodes < 0:
            raise Exception("Number of nodes must be greater than 0")
        else:
            self.num_nodes = num_nodes
            self.num_edges = 0
            self._adj =[set() for _ in range(num_nodes)]

    def _init_num_edges(self):
        """Get the number of edges"""
        edges = set()
        for node_v, nodes in self._adj.items():
            for node_w in nodes:
                edges.add(frozenset([node_v, node_w]))
        return len(edges)

    def _init(self, arg):
        """
        Init a graph with incoming text stream
        """
        edge = arg[1]
        if edge < 0:
            raise Exception("sd")
        else:
            for (nodev, nodew) in self.arg[2:]:
                self.add_edge(nodev, nodew)

class Graph():
    def __init__(self,vetices):
        self.graph = cx.defaultdict(list)
        self.V = vetices
    
    def add_edge(self, nodeA, nodeB):
        self.graph[nodeA].append(nodeB)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 创建树
def build(data):
    if len(data) == 0:
        return TreeNode(0)
    nodeQueue = []
    # 创建一根节点，并将根节点进栈
    root = TreeNode(data[0])
    nodeQueue.append(root)
    # 记录当前行节点的数量
    lineNum = 2
    # 记录当前行中数字在数组中的位置
    startIndex = 1
    # 记录数组中剩余元素的数量
    restLength = len(data) - 1
    while restLength > 0:
        for index in range(startIndex, startIndex + lineNum, 2):
            if index == len(data):
                return root
            cur_node = nodeQueue.pop()
            if data[index] is not None:
                cur_node.left = TreeNode(data[index])
                nodeQueue.append(cur_node.left)
            if index + 1 == len(data):
                return root
            if data[index + 1] is not None:
                cur_node.right = TreeNode(data[index + 1])
                nodeQueue.append(cur_node.right)
        startIndex += lineNum
        restLength -= lineNum
        # 此处用来更新下一层树对应节点的最大值
        lineNum = len(nodeQueue) * 2
    return root