class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
       arr=[i for i in range(1,len(flips)+1)]
       arr_sum=0
       flip_sum=0
       count=0 
       for i in range(len(flips)):
           arr_sum=arr_sum+arr[i]
           flip_sum=flip_sum+flips[i]
           if flip_sum==arr_sum:
               count=count+1 
       return count