class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans=0
        jewels=list(jewels)
        for jewel in jewels:
            for stone in stones:
                if stone==jewel:
                    ans+= 1 

        return ans 
        
        