class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        n = len(nums) // 2 if len(nums) % 2 == 0 else (len(nums) + 1) // 2
        for i in range  (len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1 
            else :dic[nums[i]]=1 

            if dic[nums[i]]==n:
                return nums[i]
        return 0 
        