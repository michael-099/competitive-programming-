class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-1*stone for stone in stones]
        heapify(stones)
        while len(stones)>1:
            stone1=-(heappop(stones))
            stone2=-(heappop(stones))
            winner_stone=-abs(stone1-stone2)
            heappush(stones,winner_stone)
        return -(stones[0]) if stones else 0

