'''
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
'''
class TrieNode(object):
    def __init__(self):
        self.next=dict()
        self.word=None

class Solution(object):

    def __init__(self):
        self.root=TrieNode()
        self.ans=[]

    def insert(self,word):
        node=self.root
        for i in word:
            if i not in node.next:
                node.next[i]=TrieNode()
            node=node.next[i]
        node.word=word

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        for word in words:
            self.insert(word)
        for x in xrange(len(board)):
            for y in xrange(len(board[x])):
                self.dfs(board,x,y,self.root)
        return  self.ans

    def dfs(self,board,x,y,root):
        if x<0 or x>=len(board) or y<0 or y>=len(board[x]) or board[x][y] not in root.next:
            return
        letter=board[x][y]
        root=root.next[letter]
        if root.word is not None:
            self.ans.append(root.word)
            root.word=None
        board[x][y]='#'
        self.dfs(board,x-1,y,root)
        self.dfs(board,x+1,y,root)
        self.dfs(board,x,y-1,root)
        self.dfs(board,x,y+1,root)
        board[x][y]=letter

board=[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
print Solution().findWords(board,words)

'''
Solution: brute force DFS is ok for small dataset, build a trie tree to mantain the query words is efficient for the big dataset
    when choosing the next node to traverse, no need to check each letter in the TrieNode(TLE because of 26x slower)
    remember to recory the status when backtracking
Type: Trie Tree 
'''