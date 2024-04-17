class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[-1*pile for pile in piles]
        heapify(piles)
        
        for i in range(k):
            pile=heappop(piles)
            pile=-(abs(pile)-floor(abs(pile)/2))
            heappush(piles,pile)
        return -sum(piles)


     
        