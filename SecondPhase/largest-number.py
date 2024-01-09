class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(reverse=True)
        print(nums)
        for i in range(len(nums)-1):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                     nums[i], nums[j] = nums[j], nums[i]
                
            
        num = "".join(nums)
        return num if nums[0]!="0" else "0"
        # nums = [0,0]

