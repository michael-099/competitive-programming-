class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        Max=0
        for i in range(1,len (nums)-1):
            if (nums[i]+nums[i+1]>nums[i-1] and nums[i]+nums[i-1]>nums[i+1] and nums[i-1]+nums[i+1]>nums[i]):
                Max=max(Max,(nums[i]+nums[i+1]+nums[i-1]))

        return Max

        