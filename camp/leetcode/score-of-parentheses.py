class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ''' 
On this problem, we have to keep a stack of numbers instead of a stack of parentheses for the calculation of the score.
 So, to explain how this works: every time we encounter an opening parenthesis, we will append 0 to our stack.
 When we encounter a closing parenthesis, we will work with two variables: the output variable and the value (val). 
 We will pop the top of the stack, and if it is 0, we will turn it to 1 since it is the first '()' pair, 
 which has a score of one. 
 But if it is not 0, it means that it is nested, so we will multiply it by two. 
 After doing all that, if the stack is empty, we will add the value to our output. 
 If not, we will add it to the top of the stack. Finally, we will return the output.'''
        stack=[]
        output,val=0,0 
        for i in range(len(s)):
            if s[i] =="(":
                stack.append(0)
            else:
                stack_top=stack.pop()
                if stack_top==0:
                    val=1 
                else:
                    val=stack_top*2
                if not stack:
                    output+=val
                else:
                    stack[-1]+=val
        return output
                