class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic={}
        for i in range(len(s)):
            dic[s[i]]=dic.get(s[i],0)+1
            if dic[s[i]]==2 :
                return s[i]
