class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        low,high=1,max(candies)
        max_candies=0
        def checkEqual(mid):
            kids=0
            for i in range(len(candies)):
                kids+=candies[i]//mid if mid !=0 else 0
            return kids>=k
    
        while high>=low:
            mid=(high+low)//2
            if checkEqual(mid):
                max_candies=max(max_candies,mid)
                low=mid+1  
            else:
                high=mid-1
        return max_candies
        