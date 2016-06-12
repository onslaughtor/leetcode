class Solution(object):

    def findKth(self,nums1,nums2,k):
        if len(nums1)==0:
            return nums2[k-1]
        if len(nums2)==0:
            return nums1[k-1]
        if k==1:
            return min(nums1[0],nums2[0])
        idx1=min(len(nums1),k/2)-1
        idx2=min(len(nums2),k/2)-1
        if nums1[idx1]<nums2[idx2]:
            return self.findKth(nums1[idx1+1:],nums2,k-idx1-1)
        elif nums1[idx1]>nums2[idx2]:
            return self.findKth(nums1,nums2[idx2+1:],k-idx2-1)
        elif idx1+idx2+2<k:
            return self.findKth(nums1[idx1+1:],nums2[idx2+1:],k-idx1-idx2-2)    
        else:    
            return nums1[idx1]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1)+len(nums2))%2==0:
            return (self.findKth(nums1,nums2,(len(nums1)+len(nums2))/2) \
                   +self.findKth(nums1,nums2,(len(nums1)+len(nums2))/2+1))/2.0
        else:
            return self.findKth(nums1,nums2,(len(nums1)+len(nums2))/2+1)*1.0


print Solution().findMedianSortedArrays([4,5,7],[1,2,3,6,8,9,10])
