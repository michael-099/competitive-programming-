class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high =1, max(piles)
        print(high,low)

        def canSheEatIn(mid):
            """a function to check that if koko can eat it in h hour eating mid in one hour"""
            hours=0
            for i in range(len(piles)):
                if piles[i]<mid:
                    hours+=1
                else:
                    hours+=ceil(piles[i]/mid)
            return h>=hours

        k=high
        while high >= low:
            mid = low+(high-low) // 2
            print(canSheEatIn(mid),mid)
            if canSheEatIn(mid):
                high = mid - 1
                k = min(k, mid)
            else:
                low = mid + 1

        return k
