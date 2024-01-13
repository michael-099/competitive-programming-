class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start,end,max_freq,count,res=0,0,0 ,0,0
        dic={}
        for end in range(len(s)):
            dic[s[end]]=dic.get(s[end],0)+1
            max_freq=max(max_freq,dic[s[end]])
            count =count +1 
            while (end-start+1)-max_freq>k:
                dic [s[start]]=dic[s[start]]-1
                start=start+1 
                count =count-1 
            res=max(count,res)
        return res 

        