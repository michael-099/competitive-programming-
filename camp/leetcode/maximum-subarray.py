class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        max_sum=float('inf')*-1
        for i in range(len(nums)):
            s=s+nums[i]
            max_sum=max(s,max_sum)
            if s<0 :
                s=0
        return max_sum
            
