"""
Design a search autocomplete system for a search engine. 
Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length 
n where sentences[i] is a previously typed sentence and times[i] is the corresponding 
number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c.
Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.


Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
"""
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0
        
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keywords = ""
        for i, sentence in enumerate(sentences):
            self.add_root(sentence, times[i])

    def add_root(self, sentence, t):
        p_node = self.root
        for c in sentence:
            if c not in p_node.children:
                p_node.children[c] = TrieNode()
            else:
                p_node = p_node.children
        p_node.isEnd = True
        p_node.data = sentence
        p_node.rank = t - 1

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

    # def __init__(self, sentences, times):
    #     self.root = TrieNode()
    #     self.keyword = ""
    #     for i, sentence in enumerate(sentences):
    #         self.addRecord(sentence, times[i])

    # def addRecord(self, sentence, hot):
    #     p = self.root
    #     for c in sentence:
    #         if c not in p.children:
    #             p.children[c] = TrieNode()
    #         p = p.children[c]
    #     p.isEnd = True
    #     p.data = sentence
    #     p.rank -= hot
    
    # def dfs(self, root):
    #     ret = []
    #     if root:
    #         if root.isEnd:
    #             ret.append((root.rank, root.data))
    #         for child in root.children:
    #             ret.extend(self.dfs(root.children[child]))
    #     return ret
        
    # def search(self, sentence):
    #     p = self.root
    #     for c in sentence:
    #         if c not in p.children:
    #             return []
    #         p = p.children[c]
    #     return self.dfs(p)
    
    # def input(self, c):
    #     results = []
    #     if c != "#":
    #         self.keyword += c
    #         results = self.search(self.keyword)
    #     else:
    #         self.addRecord(self.keyword, 1)
    #         self.keyword = ""
    #     return [item[1] for item in sorted(results)[:3]]