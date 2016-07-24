class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        from collections import deque
        import string
        wordList.add(endWord)
        q=deque([(beginWord,1)])
        while len(q)>0:
            x=q.popleft()
            if x[0]==endWord:
                return x[1]   
            for i in xrange(len(x[0])):
                left=x[0][:i]
                right=x[0][i+1:] 
                for j in string.lowercase:
                    y=left+j+right
                    if y in wordList:
                        q.append((y,x[1]+1))
                        wordList.remove(y)  
        return 0
                

print Solution().ladderLength('hit','cog',set(["hot","dot","dog","lot","log"]))
print Solution().ladderLength("qa","sq",set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))

 