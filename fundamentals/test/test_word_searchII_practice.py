from typing import List

def build_each_word_node(word, cur):
    for c in word:
        idx = ord(c) - ord('a')
        if not cur.nodes[idx]:
            cur.nodes[idx] = TrieNode()
        cur = cur.nodes[idx]
    return cur

def walk_all_possible_paths(root, n, m, walk):
    for i in range(n):
        for j in range(m):
            walk(j, i, root)


def build_trie_on_words(words):
    root = TrieNode()
    
    for word in words:
        cur = root
        cur = build_each_word_node(word, cur)
        cur.word = word

    return root


class TrieNode():
    def __init__(self):
        self.nodes = [None] * 26
        self.word = None

def build_each_word_node(word, cur):
    for c in word:
        idx = ord(c) - ord('a')
        if not cur.nodes[idx]:
            cur.nodes[idx] = TrieNode()
        cur = cur.nodes[idx]
    return cur


def build_trie_on_words(words):
    root = TrieNode()
    
    for word in words:
        cur = root
        cur = build_each_word_node(word, cur)
        cur.word = word
    return root


def findWords(board: List[List[str]], words: List[str]) -> List[str]:

    def dfs_traverse(x,y,node):
        if x < 0 or x == rows or y < 0 or y == cols or board[x][y] == '#':
            return
        cur = board[x][y]
        idx = ord(cur) - ord('a')
        if not node.nodes[idx]:
            return
        if node.nodes[idx].word:
            ans.append(node.nodes[idx].word)
            node.nodes[idx].word = None
        
        board[x][y] = '#'
        dfs_traverse(x + 1,y, node.nodes[idx])
        dfs_traverse(x - 1,y, node.nodes[idx])
        dfs_traverse(x,y + 1, node.nodes[idx])
        dfs_traverse(x,y - 1, node.nodes[idx])
        board[x][y] = cur

    ans = []
    root = build_trie_on_words(words)
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            dfs_traverse(i,j,root)
    
    return ans

def test_word_search_two():
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"] #Trie
    print(findWords(board,words))
    assert findWords(board,words) == ['oath','eat']

def main():
    test_word_search_two()

if __name__ == '__main__':
    main()