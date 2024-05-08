class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]]+=1

        for num in nums:
            if dic[num]==1:
                return num 