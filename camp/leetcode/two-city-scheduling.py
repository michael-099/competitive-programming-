class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        Sum=0
        for i in range(len(costs)):
            if i < len(costs)/2:
                Sum=Sum+costs[i][0]
            else :
                Sum+=costs[i][1]
        return Sum


        
        