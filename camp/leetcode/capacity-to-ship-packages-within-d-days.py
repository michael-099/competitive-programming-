class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        capacity = 100000000000

        while high >= low:
            mid = low + (high - low) // 2
            print (self.check(mid, days, weights))

            if self.check(mid, days, weights):
                high = mid - 1
                capacity = min(capacity, mid)
                print(capacity)
            else:
                low = mid + 1
        return capacity

    def check(self, mid, days, weights):
        ships,currCap=1,mid
        for weight in weights:
            if currCap-weight<0:
                ships +=1
                currCap=mid
            currCap-=weight
        return ships <= days
           
