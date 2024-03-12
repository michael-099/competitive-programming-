class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) + 7
        odd = n // 2
        even = n // 2 + n % 2
        # in the last two lines we are trying to find how many odd places and even places are there
        return (self.binary(5, even) % mod * self.binary(4, odd) % mod) % mod

    def binary(self ,val, n):
        mod = (10**9) + 7
        if n == 0:
            return 1
        
        if n % 2 == 0:
            return self.binary((val * val) % mod, (n // 2))
        else:
            return val * self.binary((val * val) % mod, (n - 1) // 2)
