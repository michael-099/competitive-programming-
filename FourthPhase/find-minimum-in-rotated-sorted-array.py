class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1
        while right > left:
            mid = (right + left) // 2
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1
            min_num = mid

        return nums[left]
