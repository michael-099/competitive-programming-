class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        right,left=0,0
        for i in range (len(nums1)+len(nums2)):
            if nums1[left]==nums2[right]:
                return nums1[left]
            elif nums1[left]>nums2[right] and right<len(nums2)-1:
                right+=1 
            elif  nums1[left]<nums2[right] and left<len(nums1)-1:
                left+=1 
        return -1
