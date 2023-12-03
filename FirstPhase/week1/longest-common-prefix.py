class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr=[]
        
        if len(strs)==1:
            return strs[0]
        for i in range (len(strs)-1):
            s=""
            if strs[i]=="" or strs[i+1] ==""or strs[i][0]!=strs[i+1][0]:
                    return ""
            for j in range (min(len(strs[i]),len(strs[i+1]))):
                if strs[i][j]!=strs[i+1][j]:
                    break
                s=s+strs[i][j]
            arr.append(s)
        return min(arr) if arr else ""
                
            

