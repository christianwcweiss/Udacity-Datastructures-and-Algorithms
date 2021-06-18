#from ipywidgets import widgets
#from IPython.display import display
#from ipywidgets import interact


class TrieNode:
    def __init__(self, value = '', end_of_word=False):
        self.value = value
        self.alphabet_dict = {
            'a': None,
            'b': None,
            'c': None,
            'd': None,
            'e': None,
            'f': None,
            'g': None,
            'h': None,
            'i': None,
            'j': None,
            'k': None,
            'l': None,
            'm': None,
            'n': None,
            'o': None,
            'p': None,
            'q': None,
            'r': None,
            's': None,
            't': None,
            'u': None,
            'v': None,
            'w': None,
            'x': None,
            'y': None,
            'z': None
        }
        self.end_of_word = end_of_word

    def insert(self, char):
        if char not in self.alphabet_dict:
            return "Couldn't be added!"
        else:
            self.alphabet_dict[char] = TrieNode(char)

    def suffixes(self):
        suffixes = set([])
        st = [(self, "")]
        while st:
            node, suffix = st.pop()
            for k, v in node.alphabet_dict.items():
                if v:
                    st.append((v, suffix + k))
                if node.end_of_word:
                    suffixes.add(suffix)
        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        word = word.lower()
        for c in word:
            if c not in set("abcdefghijklmnopqrstuvwxyz"):
                return None
        curr_node = self.root
        for i, c in enumerate(word):
            if curr_node.alphabet_dict.get(c):
                curr_node = curr_node.alphabet_dict[c]
            else:
                next_node = TrieNode(c, i == len(word) - 1)
                curr_node.alphabet_dict[c] = next_node
                curr_node = next_node

    def find(self, prefix):
        current_node = self.root
        for c in prefix:
            if c not in current_node.alphabet_dict.keys():
                return None
            else:
                current_node = current_node.alphabet_dict[c]
        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.root.suffixes())

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            ans = prefixNode.suffixes()
            return ans
    return []

#interact(f, prefix='');

#own test_cases
print("Test Case 1 - empty list for empty prefix")
solution = []
output = sorted(f(''))
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - find all elements starting with t")
solution = ['rie', 'rigger', 'rigonometry', 'ripod']
output = sorted(f('t'))
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - special character words are not added")
solution = None
output = MyTrie.insert("*1234")
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - special character words are not added and can't be found")
solution = []
output = sorted(f('*'))
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - add same word multiple times")
word_list = ["factory", "factory", "factory", "factory", "factory", "factory", "factory", "factory"]
for word in word_list:
    MyTrie.insert(word)
solution = ['actory', 'un', 'unction']
output = sorted(f('f'))
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 6 - add capital letter word")
word_list = ["FACTORY", "FORCE"]
for word in word_list:
    MyTrie.insert(word)
solution = ['actory', 'orce', 'un', 'unction']
output = sorted(f('f'))
print("Output: {0}".format(output))
assert(output == solution)
print("TestCase 6 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")