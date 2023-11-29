class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # if num<3:
        #     return []
        # Sum=6
        # for end in range(3,(num+1)//2):
        #     Sum=Sum-(end-3)
        #     Sum=Sum+end
        #     if (Sum== num):
        #         return [end-1,end,end+1]
        # return []
        x='inf'
        if (num-3)%3==0:
            x=(num-3)//3
        return [] if x == 'inf' else [x,x+1,x+2]


        

        