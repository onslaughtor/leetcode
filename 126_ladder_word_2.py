class Solution(object):
    def ladderLength(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord==endWord:
            return [[beginWord,endWord]]
        from collections import deque
        import string
        wordlist.add(endWord)
        child=dict()
        dis=dict()
        for i in wordlist:
            child[i]=[]
            dis[i]=len(wordlist)+1
        q=deque([beginWord])
        dis[beginWord]=1    
        child[beginWord]=[]
        while len(q)>0:
            x=q.popleft()
            if x==endWord:
                break   
            for i in xrange(len(x)):
                left=x[:i]
                right=x[i+1:] 
                for j in string.lowercase:
                    y=left+j+right
                    if y in wordlist:
                        if dis[x]+1<=dis[y]:
                            child[x].append(y)
                            if dis[x]+1<dis[y]:  
                                dis[y]=dis[x]+1  
                                q.append(y)

        return self.generate(child,beginWord,endWord)
  

    def generate(self,child,beginWord,endWord):
        if beginWord==endWord:
            return [[endWord]]
        ans=[]
        for i in child[beginWord]:
            tmp=self.generate(child,i,endWord)
            for l in tmp:
                ans.append([beginWord]+l)
        return ans


 

print Solution().ladderLength('hot','trg',set(["hot","dog","dot"]))
# print Solution().ladderLength('hit','cog',set(["hot","dot","dog","lot","log"]))
# print Solution().ladderLength("qa","sq",set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))

 