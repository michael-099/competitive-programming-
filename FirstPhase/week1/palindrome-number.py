class Solution:
    def isPalindrome(self, x: int) -> bool:
        start=0
        x=str(x)
        end= len(x)-1
        while end>start:
            if x[start]!=x[end]:
                return False 
            start=start+1 
            end=end-1 
            
        return True 
        