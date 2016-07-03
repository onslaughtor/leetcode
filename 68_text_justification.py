class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth==0:
            return [""]
        left,right=0,0
        cnt=0
        space=0
        res=[]
        while right<len(words):
            if cnt+space+len(words[right])>maxWidth:
                if left+1==right:
                    res.append(words[left]+' '*(maxWidth-len(words[left])))
                else:
                    space=(maxWidth-cnt)/(right-left-1)
                    more_space=(maxWidth-cnt)%(right-left-1)
                    s=''
                    for i in range(right-left):
                        s+=words[left+i]
                        if left+i<right-1:
                            s+=' '*space
                        if i<more_space:
                            s+=' '
                    res.append(s)
                left=right
                cnt=0
                space=0
            cnt+=len(words[right])
            space+=1
            right+=1
        
        s=''
        for i in range(left,right-1):
            s+=words[i]+' '
        s+=words[right-1]+' '*(maxWidth-cnt-space+1)
        res.append(s)
        return res

print Solution().fullJustify(["What","must","be","shall","be."],12)
print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)
print Solution().fullJustify(['a'],1)
print Solution().fullJustify([''],0)