class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high,target=0,len(nums)-1,nums[0]

        while high>low:
            mid=low+(high-low)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]
    
            
            
         
            