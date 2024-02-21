class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=='+'or token=='-' or token== '*' or token== '/':
                if token=="+":
                    val1=stack.pop()
                    val2=stack.pop()
                    val=val2+val1
                    stack.append(val)
                    print(stack[-1])

                elif token=="-":
                    val1=stack.pop()
                    val2=stack.pop()
                    val=val2-val1
                    stack.append(val)
                    print(stack[-1])

                elif token=="*":
                    val1=stack.pop()
                    val2=stack.pop()
                    val=val2*val1
                    stack.append(val)
                    print(stack[-1])

                elif token=="/":
                    val1=stack.pop()
                    val2=stack.pop()
                    val=ceil(val2/val1) if( val1>0 and val2<0) or( val1<0 and val2>0) else val2//val1
                    stack.append(val) 
                    print(stack[-1])
            else:
                stack.append(int(token))
        return stack.pop()

        #         operations_stack.append(token)
        # nums_stack=[]
        # operations_stack=[]
        # res=0
       
        # for token in tokens:
        #     if token=='+'or token=='-' or token== '*' or token== '/':
        #         operations_stack.append(token)
        #     else :
        #         nums_stack.append(int(token))
        # print(operations_stack,nums_stack)
        # res=nums_stack.pop()
        # # operations_stack.reverse()
        # for i in range (len(operations_stack)):
        #  if token=='+'or token=='-' or token== '*' or token== '/':
        #     if operations_stack[i]=="+":
        #         res+=nums_stack[i+1]
        #         print(res)

        #     elif operations_stack[i]=="-":
        #         res-=nums_stack[i+1]
        #         print(res)

        #     elif operations_stack[i]=="*":
        #         res=res*nums_stack[i+1]
        #         print(res)

        #     elif operations_stack[i]=="/":
        #         res=res/nums_stack[i+1]
        #         print(res)

        # return res

        
        