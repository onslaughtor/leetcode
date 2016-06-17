class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans=[]
        if len(words)==0:
            return ans
        m=len(words[0])
        n=m*len(words)   
        if n>len(s):
            return ans

        for i in range(m):
            d={}
            cnt=0
            for w in words:
                if w not in d:
                    d[w]=1
                else:
                    d[w]+=1
            for j in range(i,i+n ,m):
                sub=s[j:j+m]
                if sub in d:
                    d[sub]-=1
                    if d[sub]==0:
                        cnt+=1
                    if d[sub]==-1:
                        cnt-=1
            if cnt==len(d):
                ans.append(i) 
            for j in range(i+m,len(s)-n+1,m):
                sub=s[j-m:j]
                # print i,j,s[j-m:j],s[j+n-m:j+n]
                if sub in d:
                    d[sub]+=1
                    if d[sub]==0:
                        cnt+=1
                    if d[sub]==1:
                        cnt-=1
                sub=s[j+n-m:j+n]
                if sub in d:
                    d[sub]-=1
                    if  d[sub]==0:
                        cnt+=1
                    if  d[sub]==-1:
                        cnt-=1
                # print cnt,d
                if cnt==len(d):
                    ans.append(j)           
        return ans
    
print Solution().findSubstring('wordgoodgoodgoodbestword',["word","good","best","good"])

