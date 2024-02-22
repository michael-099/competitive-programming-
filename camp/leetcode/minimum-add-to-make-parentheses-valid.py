class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        '''on this one we need to make the parenttheses by adding a closing and openning bracket for the 
        invalid ones and we count that'''
        stack =[]
        count=0
        for p in s :
            if p =='(':
                stack.append('(')
            elif p==')' and stack:
                if  stack[-1]=='(':
                    stack.pop()
            elif p==')' and stack :
                if stack[-1]==')':
                    count+=1 
            elif p==")" and not stack:
                count+=1

        return len(stack)+count
            

