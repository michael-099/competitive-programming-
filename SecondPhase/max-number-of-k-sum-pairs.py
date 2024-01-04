class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right=0,len(nums)-1
        count=0 
        # print(nums)
        while left<right:   
            # print(nums[left],nums[right])
            # print(left,right )
            if nums[left]+nums[right]>k:
                right=right-1
            elif nums[left]+nums[right]<k:
                left=left+1 
            else:
                left=left+1
                right=right-1
                count=count+1
           
        return count 
        
            
