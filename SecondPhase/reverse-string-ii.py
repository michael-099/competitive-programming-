class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string=list(s)
        for i in range(0,len(string),2*k):
            start=i 
            end=min(i+k-1,len(string)-1 )
            while end>start:
                string[start],string[end]=string[end],string[start]
                start+=1
                end-=1 
        return "".join(string)
        