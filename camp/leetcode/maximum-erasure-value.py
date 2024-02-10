class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start=0
        dic={}
        sum_=0
        res=0
        for end in range(len(nums)):
            while nums[end] in dic and dic[nums[end]]>0:
                sum_-=nums[start]
                dic[nums[start]]-=1
                start=start+1
            if nums[end] not in dic or dic[nums[end]]==0:
                sum_+=nums[end]
                dic[nums[end]]=dic.get(nums[end],0)+1
                res=max(res,sum_)
        return res
            


        