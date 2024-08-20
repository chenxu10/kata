from typing import List

class TrieNode:
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

def walk_all_possible_paths(root, n, m, walk):
    for i in range(n):
        for j in range(m):
            walk(j, i, root)

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    
    for word in words:
        cur = root
        cur = build_each_word_node(word, cur)
        cur.word = word
    
    n, m = len(board), len(board[0])
    ans = []
    
    def walk(x, y, node):
        # terminate at leaf across boundaries or visited
        if x < 0 or x == m or y < 0 or y == n or board[y][x] == '#':
            return
        
        cur = board[y][x]
        next_node = node.nodes[ord(cur) - ord('a')]
        if not next_node:
            return
        
        if next_node.word:
            ans.append(next_node.word)
            next_node.word = None
        
        board[y][x] = '#'
        walk(x + 1, y, next_node)
        walk(x - 1, y, next_node)
        walk(x, y + 1, next_node)
        walk(x, y - 1, next_node)
        board[y][x] = cur

    walk_all_possible_paths(root, n, m, walk)
    
    return ans



def test_word_search_two():
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    print(findWords(board,words))
    assert findWords(board,words) == ['oath','eat']

def main():
    test_word_search_two()

if __name__ == '__main__':
    main()