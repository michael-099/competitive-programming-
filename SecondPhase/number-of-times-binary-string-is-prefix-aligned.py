class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
       arr_sum=0
       flip_sum=0
       count=0 
       for i in range(len(flips)):
           arr_sum+=i+1
           flip_sum=flip_sum+flips[i]
           if flip_sum==arr_sum:
               count=count+1 
       return count