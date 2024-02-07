class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[0]*len(nums)
        a[0]=nums[0]
        for i in range(1,len(nums)):
            a[i]=a[i-1]+nums[i]
        return a
