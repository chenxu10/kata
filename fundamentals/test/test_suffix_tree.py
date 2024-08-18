class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.start = None
        self.end = None
        self.suffix_index = None

class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode()
        self.text = text
        self.build_tree()

    def build_tree(self):
        for i in range(len(self.text)):
            self._insert_suffix(i)

    def _insert_suffix(self, suffix_start):
        current = self.root
        for i in range(suffix_start, len(self.text)):
            char = self.text[i]
            if char in current.children:
                current = current.children[char]
            else:
                new_node = SuffixTreeNode()
                new_node.start = i
                new_node.end = len(self.text)
                new_node.suffix_index = suffix_start
                current.children[char] = new_node
                current = new_node

    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def test_suffix_tree():
    tree = SuffixTree("banana$")
    assert tree.search("ana") == True
    assert tree.search("na$") == True
    assert tree.search("") == True
    assert tree.search("cdf") == False

def main():
    test_suffix_tree()

if __name__ == '__main__':
    main()
    # longest common subsequence