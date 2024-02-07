class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        running_sum=0 
        prefix_sum=[]
        prefix_sum_backward=[0]*len(nums)
        for i in range(len(nums)):
            running_sum+=nums[i]
            prefix_sum.append(running_sum)
        running_sum=0
        for i in range(len(nums)-1,-1,-1):
            running_sum+=nums[i]
            prefix_sum_backward[i]=running_sum
        for i in range(len(nums)):
            if prefix_sum[i]==prefix_sum_backward[i]:
                return i
        return -1
            

        