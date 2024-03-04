class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """we will initialize 3 pointers  the left pointer at index 0  the right pointer at index 1 
         and the i pointer at index 2 then as the ith pointer move one index also the right pointer will move
         one step and the left pointer will going to increment while the sum of nums[left] and nums[right] less than
          the nums[i] when the opposite is true we will chake every less subbarray by moving the right pointer till left+1 
          and we will add left-right to the answer variable and finaly we will going to return the answer variable"""
        nsot = 0
        nums.sort()

        for i in range(2, len(nums)):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    nsot += right - left
                    # print(f"left={left} right={right} i={i}")
                    # print(nsot)
                    right -= 1
                else:
                    left += 1

        return nsot
