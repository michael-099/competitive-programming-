class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1 
            else :
                dic[nums[i]]+=1
        for key,value in dic.items():
            if value == 1:
                return key 
        return 0
    