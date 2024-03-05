class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)

        for index, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(index)

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
        return res
