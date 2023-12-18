class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        result=0
        for i in range(len(nums)):
            count=0
            if nums[i]-1 not in n:
                next_seq=1
                while nums[i]+next_seq in n:
                    count=count +1 
                    next_seq+=1
                result=max(result,count+1)
        return result 