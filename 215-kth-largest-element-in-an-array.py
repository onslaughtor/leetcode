'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quick(nums,0,len(nums)-1,k)
        # return self.conquer(nums,0,len(nums)-1,k)[-1]
        
    def quick(self,nums,l,r,k):
        idx=random.randint(l, r)
        nums[idx],nums[r]=nums[r],nums[idx]
        pivot=nums[r]
        i,j=l,r
        while i<j:
            if nums[i]>=pivot:
                j-=1
                nums[i],nums[j]=nums[j],nums[i]
            else:
                i+=1
        m=r-j+1
        if m==k:
            return pivot
        if m<k:
            return self.quick(nums,l,j-1,k-m)
        else:
            return self.quick(nums,j,r-1,k)
        
        
        
    def conquer(self,nums,left,right,k):
        if left==right:
            return [nums[left]]
        if right-left+1<k:
            k=right-left+1
        mid=(left+right)/2
        a=self.conquer(nums,left,mid,k)
        b=self.conquer(nums,mid+1,right,k)
        ans=[]
        i=0
        j=0
        while len(ans)<k :
            if i==len(a) or(j<len(b) and b[j]>a[i]):
                ans.append(b[j])
                j+=1
            else:
                ans.append(a[i])
                i+=1
        return ans
                
            