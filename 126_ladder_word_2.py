from collections import deque
import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordlist.add(endWord)
        trace={i:[] for i in wordlist}
        trace[beginWord]=[]
        level={i:-1 for i in wordlist}
        level[beginWord]=0
        q=deque([beginWord])
        while len(q)>0:
            x=q.popleft()
            if x==endWord:
                break   
            for i in xrange(len(x)):
                left=x[:i]
                right=x[i+1:] 
                for j in string.lowercase:
                    y=left+j+right
                    if y in wordlist and (level[y]==-1 or level[x]+1==level[y]):
                        if level[y]==-1:
                            q.append(y)
                            level[y]=level[x]+1
                        trace[x].append(y)
        return self.backtrack(trace,beginWord,endWord)
  

    def backtrack(self,trace,beginWord,endWord):
        if beginWord==endWord:
            return [[endWord]]
        ans=[]
        for i in trace[beginWord]:
            tmp=self.backtrack(trace,i,endWord)
            for l in tmp:
                ans.append([beginWord]+l)
        return ans


 

# print Solution().ladderLength('hot','trg',set(["hot","dog","dot"]))
print Solution().ladderLength('hit','cog',set(["hot","dot","dog","lot","log"]))
# print Solution().ladderLength("qa","sq",set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))

 