class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # base case
        if n==1:
            return True
        if n<1:
            return False 
        n=n/2
        return self.isPowerOfTwo(n)
            
        