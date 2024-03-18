class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=0,x
        while high>=low:
            mid=(low+high)//2
            if mid*mid>x:
                high=mid-1
            elif mid*mid<x:
                low=low+1
            else :
                return mid
        return low-1
