'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
'''
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        prefix=dict()
        for w in wordList:
            for i in xrange(len(w)):
                tmp=w[:i]+'_'+w[i+1:]
                if tmp not in prefix:
                    prefix[tmp]=[]
                prefix[tmp].append(w)
                
        queue=deque([(beginWord,1)])
        while len(queue)>0:
            w,d=queue.popleft()
            for i in xrange(len(w)):
                tmp=w[:i]+'_'+w[i+1:]
                for word in prefix[tmp]:
                    if word==endWord:
                        return d+1
                    if word in wordList:
                        queue.append((word,d+1))
                        wordList.remove(word)
        return 0
                        

print Solution().ladderLength('hit','cog',set(["hot","dot","dog","lot","log"]))
print Solution().ladderLength("qa","sq",set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))

 