
class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class SuffixTree:
    def __init__(self, s):
        self.s = s
        self.root = self._build_tree()

    def _build_tree(self):
        root = SuffixTreeNode()
        for i in range(len(self.s)):
            self._insert_suffix(self.s[i:],root)
        return root
    
    def _insert_suffix(self, suffix, root):
        cur = root
        for c in suffix:
            if c not in cur.children:
                cur.children[c] = SuffixTreeNode()
            cur = cur.children[c]
        cur.is_end = True
        
    
    def search(self, suffix):
        cur = self.root
        for c in suffix:
            if c not in cur.children:
                return False
            cur = cur.children[c]            
        return True

def test_suffix_tree():
    tree = SuffixTree("banana$")
    root = tree._build_tree()
    assert root.children['b'].is_end==False
    assert tree.search("ana") == True
    assert tree.search("cdf") == False
    assert tree.search("banana$") == True
    assert tree.search("Xana") == False
    # assert tree.search("na$") == True
    # assert tree.search("") == True

def main():
    test_suffix_tree()

if __name__ == "__main__":
    main()