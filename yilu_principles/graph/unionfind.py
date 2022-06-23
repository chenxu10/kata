# Example
# 李白
# 王昌龄 数年同笔砚，兹夕间衾裯
# 孟浩然 吾爱孟夫子，风流天下闻
# 杜甫 三夜频梦君，情亲见君意
#
#{lilei, hanmeimei, laowang,xiaohong,xiaohong}
# Disjoin Set

class UnionFindQuickFinder():
    def __init__(self, numElements):
        self.id = [i for i in range(numElements)]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

    def is_connected(self, p, q):
        return self.id[p] == self.id[q]

def test_UnionFindQuickFinder():
    UF = UnionFindQuickFinder(5)
    UF.union(0,1)    
    UF.union(1,2)
    UF.union(3,4)

class UnionFindQuickUnion():
    # construct
    def __init__(self, numElements):
        self.parent = {} #{3:2}
        self.count = 0
        self.weight = list(range(numElements))

    def set_parent(self,x):
        if x not in self.parent:
            self.parent[x] = x

    # find_parent
    def find_parent(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]] # cache
            x = self.parent(x)                           # weight
        return self.parent[x]

    def union(self, p, q):
        return self.find_parent[p] == self.find_parent[q]

    # count
    def count(self):
        return self.count()

def test_UnionFindQuickUnion():
    UF = UnionFindQuickUnion(5)
    UF.set_parent(0)
    UF.set_parent(1)
    UF.set_parent(2)
    UF.set_parent(3)
    UF.set_parent(4)
    UF.union(0,1)    
    UF.union(3,4)
    print(UF.is_connected(0,2))
    print(UF.is_connected(3,1))
    print(UF.count)

#[2,2,2,3,4]
# 0 1 2 3 4
# classic leetcode 200, leetcode 305 
# Choose underlying algorithm array or list
# What information you want to add weights
# Path caching or hashmap to store memory

if __name__ == '__main__':
    # test_UnionFindQuickFinder()
    test_UnionFindQuickUnion()