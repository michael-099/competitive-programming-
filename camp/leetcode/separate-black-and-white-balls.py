class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros=0
        count=0
        for i in range(len(s)):
            if s[i]=="0":
                zeros+=1
        for i in range(len(s)):
            if s[i] =="1":
                count+=zeros
            else:
                zeros-= 1 
        return count
        