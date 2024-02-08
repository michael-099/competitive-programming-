class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix={0:1}
        running_sum=0
        count=0 

        for i in range(len(nums)):
            running_sum+=nums[i]
            if running_sum-goal in prefix:
                count+=prefix[running_sum-goal]
            prefix[running_sum]=prefix.get(running_sum,0)+1 
        return count
        
            
            
            
      

