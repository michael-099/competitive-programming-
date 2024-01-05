class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        count = 0
        temp=[capacity[i]-rocks[i] for i in range (len(capacity))]
        temp.sort()
        for i in range(len(temp)):
            if temp[i]<= additionalRocks:
                count = count + 1
                additionalRocks -= temp[i]   
        return count
