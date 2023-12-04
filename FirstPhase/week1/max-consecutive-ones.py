class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res,count=0,0
        for i in nums:
            if  i==1 :
                count=count+1 
            else:count=0
            res=max(count,res)
        return res
        