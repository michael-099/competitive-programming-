class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum_=0 
        count=0

        for i in range(len(costs)):
            sum_+=costs[i]
            if sum_ <=coins:
                count=count+1 
        return count 
             
        