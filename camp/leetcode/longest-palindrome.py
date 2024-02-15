class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic={}
        count=0
        Flag=False
        for i in range(len(s)):
            dic[s[i]]=dic.get(s[i],0)+1
        dic=dict(sorted(dic.items(),key=lambda x:x[1]))
        for i in dic:
            if dic[i]//2>0:
                count+=(dic[i]//2)*2
                dic[i]-=(dic[i]//2)*2
            if dic[i]==1:
                Flag=True
        return count if Flag==False else count+1
            

    
    

        



        