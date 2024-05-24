class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False 
        if s=="": return True 
        s_pointer=0
        t_pointer=0
       

        while s_pointer < len(s) and t_pointer < len(t):
            if s_pointer==(len(s)-1) and s[s_pointer]==t[t_pointer]:
                return True

            elif s[s_pointer]==t[t_pointer]:
                s_pointer+=1 
            
            t_pointer+=1
        
        return False

            
        