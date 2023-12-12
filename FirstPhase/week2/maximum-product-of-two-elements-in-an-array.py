class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max=max(nums)
        nums.remove(Max)
        print(nums)
        Max2=max(nums)
        return( Max-1)*(Max2-1)
        