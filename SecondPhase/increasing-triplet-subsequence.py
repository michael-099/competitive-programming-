class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_left = [float('inf')] * len(nums)
        max_right = [float('-inf')] * len(nums)

        min_left[0] = nums[0]   
        max_right[-1] = nums[-1]

        for i in range(1, len(nums)):
            min_left[i] = min(min_left[i - 1], nums[i])

        for i in range(len(nums) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], nums[i])  

        for i in range (len(nums)):
            if min_left[i]<nums[i]<max_right[i]:
                return True 
        return False
        