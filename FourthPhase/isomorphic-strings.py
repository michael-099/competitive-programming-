class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
    
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]]!=t[i]:
                return False
            else:
                dic[s[i]]=t[i]
        dic={}
        for i in range(len(s)):
            if t[i] in dic and dic[t[i]]!=s[i]:
                return False
            else:
                dic[t[i]]=s[i]
        return True
        