class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        running_sum=0 
        count=0

        for i in range(len(nums)):
            running_sum+=nums[i]
            if running_sum-k in prefix:
                count+=prefix[running_sum-k]
            prefix[running_sum]=prefix.get(running_sum,0)+1
        return count
        