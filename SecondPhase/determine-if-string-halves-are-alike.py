class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left,right,right_count,left_count=0,len(s)-1,0,0
        vouls={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while(right>left):
            if s[right] in vouls:
                right_count+=1
            if s[left] in vouls:
                left_count+=1
            right-=1 
            left+=1 
        return left_count==right_count
        
        