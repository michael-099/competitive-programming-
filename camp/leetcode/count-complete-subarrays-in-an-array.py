class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        numSet=set(nums)
        n=len(numSet)
        count = 0 
        dCount=0
        
        for i in range(len(nums)):
            distinct=set()
            for j in range(i,len(nums)):
                distinct.add(nums[j])
                if len(distinct)==n:
                    dCount+=1 
        return dCount
                
                



        return count 