class Trie:
    def __init__(self):
        self.nodes = [None] * 26
        self.word = None
    
    def build_word(self, word, cur):
        for c in word:
            idx = ord(c) - ord('a')
            next_node = cur.nodes[idx]
            if not next_node:
                next_node = Trie()
            cur = next_node
        return cur


def test_trie():
    t = Trie()
    cur = t.build_word('bc',t)
    print(cur.nodes)

def main():
    test_trie()
if __name__ == '__main__':
    main()
