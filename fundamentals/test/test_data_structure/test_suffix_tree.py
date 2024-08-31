class SuffixNodes:
    def __init__(self) -> None:
        self.nodes = [None] * 26
        self.word = None

class SuffixTree:
    def build_suffix_tree(self,word,cur):
        return suffix_node

def test_suffix_tree():
    tree = SuffixTree("banana$")
    assert tree.search("ana") == True
    assert tree.search("na$") == True
    assert tree.search("") == True
    assert tree.search("cdf") == False

def main():
    pass
    #test_suffix_tree()

if __name__ == '__main__':
    main()
    # longest common subsequence(leetcode14)