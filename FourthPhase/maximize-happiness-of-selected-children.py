class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res=0
        for i in range(k):
            val=happiness.pop()
            if val>=i:
                res+=val-i    
        return res
        


