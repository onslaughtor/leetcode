'''
Given an integer array of size n, find all elements that appear more than n/3 times. 
The algorithm should run in linear time and in O(1) space.
'''
import heapq

class Solution(object):
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        n=len(nums)
        if n==0:
            return []
        k=n/3
        if n%3>0:
            k+=1
        a=self.kthElement(nums,k)
        b=self.kthElement(nums,n-k+1)
        print a,b
        if nums.count(a)>n/3:
            ans.append(a)
        if a!=b and nums.count(b)>n/3 :
            ans.append(b)
        return ans 

    def majorityElement(self, nums):
        n=len(nums)
        a=0 
        b=0
        na=0
        nb=0
        for i in nums:
            if i==a:
                na+=1
            elif i==b:
                nb+=1
            elif na==0:
                a=i
                na=1
            elif nb==0:
                b=i
                nb=1
            else:
                na-=1
                nb-=1
        ans=[]
        if nums.count(a)>n/3:
            ans.append(a)
        if a!=b and nums.count(b)>n/3 :
            ans.append(b)
        return ans 
            

    def kthElement(self,nums,k):
        queue=[]
        for i in nums:
            heapq.heappush(queue,i)
            if len(queue)>k:
                heapq.heappop(queue)
        return heapq.heappop(queue)
        
    def kthElement2(self,nums,k):
        left=0
        right=len(nums)-1
        while True:
            p=self.partition(nums,left,right)
            if p+1==k:
                return nums[p]
            elif p+1>k:
                right=p-1
            else:
                left=p+1
                
        
    def partition(self,nums,left,right):
        pivot=nums[left]
        l=left+1
        r=right
        while l<=r:
            if nums[l]>pivot and nums[r]<pivot:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
                l+=1
            elif nums[l]<=pivot:
                l+=1
            else:
                r-=1
        nums[left],nums[r]=nums[r],nums[left]
        return r
        
'''
Solution: it's obvious there is at most two elements and it has to be in [n/3th smallest,n/3th biggest]
    so it's to find the Kth Elements in an array.
    quick sort is O(n^2) when the data is special and heapsort is stable O(nlogK)
    but a better solution is to conteract with each other and the left ones are candidates
Type: Sort
Comment: good idea to counteract, good application of Kth Element solution
'''