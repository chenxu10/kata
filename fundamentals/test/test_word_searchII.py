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


def build_trie_on_words(words):
    root = TrieNode()
    
    for word in words:
        cur = root
        cur = build_each_word_node(word, cur)
        cur.word = word
    return root

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    root = build_trie_on_words(words)
    result = []
    m = len(board)
    n = len(board[0])
    
    def walk(row, col, node):
        
        if row < 0 or row >= m or col < 0 or col >=n or board[row][col] == '#':
            return 
        
        cur = board[row][col]
        next_node = node.nodes[ord(cur) - ord('a')]
        if not next_node:
            return
        
        if next_node.word:
            result.append(next_node.word)
            next_node.word = None

        board[row][col] = '#'
        walk(row - 1, col, next_node)
        walk(row + 1, col, next_node)
        walk(row, col + 1, next_node)        
        walk(row, col - 1, next_node)
        board[row][col] = cur

    walk_all_possible_paths(root, m, n, walk)
    return result

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
    #test_word_search_two()
    curnode = build_each_word_node('aac', TrieNode())
    print(curnode.nodes)#print(root.nodes[0].nodes[0].nodes[1].word)

if __name__ == '__main__':
    main()