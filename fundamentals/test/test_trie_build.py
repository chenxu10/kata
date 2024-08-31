class Trie:
    def __init__(self):
        self.nodes = [None] * 26
        self.word = None
    
def build_word(word, root):
    cur = root
    for c in word:
        idx = ord(c) - ord('a')
        if not cur.nodes[idx]:
            cur.nodes[idx] = Trie()
        cur = cur.nodes[idx]
    cur.word = word
    return root

def test_trie():
    t = Trie()
    cur = build_word('abc',t)
    print(cur.nodes[0].nodes[1])

def main():
    test_trie()
if __name__ == '__main__':
    main()
