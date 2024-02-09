class Solution:
    def pivotInteger(self, n: int) -> int:
        running_sum=0
        prefix=[]
        suffix=[0]*n
        pivot=-1
        for i in range(n):
            running_sum+=i+1
            prefix.append(running_sum)
        # print(prefix)
        running_sum=0
        for i in range(n,0,-1):
            running_sum+=i
            suffix[i-1]=running_sum
        # print(suffix)
            

        for i in range(len(prefix)):
            if prefix[i]==suffix[i]:
                 pivot=i+1
                 break
            
        return pivot
        

        
        