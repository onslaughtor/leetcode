'''
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
'''

class TrieNode(object):
    def __init__(self):
        self.next=dict()
        self.isWord=False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root=TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node=self.root
        for i in word:
            if i not in node.next:
                node.next[i]=TrieNode()
            node=node.next[i]
        node.isWord=True
    
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.match(self.root,word,0)
        
    def match(self,node,word,idx):
        if idx==len(word):
            return node.isWord
        if word[idx]=='.':
            for i in node.next:
                if self.match(node.next[i],word,idx+1):
                    return True
        elif word[idx] in node.next:
            return self.match(node.next[word[idx]],word,idx+1)
        return False

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("a")
# wordDictionary.search("a")
wordDictionary.search("a.")
wordDictionary.search(".a")

'''
Type: Trie Tree
'''