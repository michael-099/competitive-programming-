class Solution:
    def maxScore(self, s: str) -> int:
        left=0 
        right=s.count("1")
        Sum=[0]*(len(s))
        for i in range(len(s)):
            if s[i]=="0":
                left+=1
            Sum[i]+=left

        for i in range(len(s)):
            if s[i]=="1":
                right-=1
            Sum[i]+=right
        
        return max(Sum[:len(Sum)-1])
            
            
        