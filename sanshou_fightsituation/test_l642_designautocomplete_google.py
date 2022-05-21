class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0
        
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.addRecord(sentence, times[i])

    def addRecord(self, sentence, hot):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        p.data = sentence
        p.rank -= hot
    
    def dfs(self, root):
        ret = []
        if root:
            if root.isEnd:
                ret.append((root.rank, root.data))
            for child in root.children:
                ret.extend(self.dfs(root.children[child]))
        return ret
        
    def search(self, sentence):
        p = self.root
        for c in sentence:
            if c not in p.children:
                return []
            p = p.children[c]
        return self.dfs(p)
    
    def input(self, c):
        results = []
        if c != "#":
            self.keyword += c
            results = self.search(self.keyword)
        else:
            self.addRecord(self.keyword, 1)
            self.keyword = ""
        return [item[1] for item in sorted(results)[:3]]

def test_autocomplete():
    sentences = ["i love you","island","iroman","i love leetcode"]
    times = [5,3,2,2]
    AutoCompleter = AutocompleteSystem(sentences, times)
    assert AutoCompleter.input("i") == [
        "i love you",
        "island",
        "i love leetcode"]
    assert AutoCompleter.input(" ") == ["i love you","i love leetcode"]
    assert AutoCompleter.input("a") == []

if __name__ == '__main__':
    test_autocomplete()