class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left,right,count=0,0,0
        if len(s)==0 or len(g)==0:
            return 0
        for i in range(len(g)+len(s)):
           
            if g[left]<=s[right]:
                left+=1 
                right+=1 
                count+=1 
            else:
                right+=1 
            if len(g)==left or len(s)==right:
                return count 
           
        return count 

            

        