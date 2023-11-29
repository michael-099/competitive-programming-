class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for i in range(len(s)):
            dic[s[i]]=dic.get(s[i],0)+1
        for x in range (len(s)):
            if dic[s[x]]==1:
                return indexOf(s,s[x])
        return -1
            