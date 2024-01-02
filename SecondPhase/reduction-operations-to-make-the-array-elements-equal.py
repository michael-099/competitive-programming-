class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
    #     def SecondLargest(self,nums:List[int]):
    #         nums=sorted(set(nums),reverse=True)
    #         return nums[1] if len(nums)>1 else None 
    #     Flag=True 
    #     count=0

    #     while Flag:
    #         nums.sort(reverse=True)
    #         if SecondLargest(self,nums):
    #             nums[0]=SecondLargest(self,nums)
    #             count+=1 
    #         else :
    #             Flag=False
    #     return count 
        nums.sort()
        answer,temp=0 ,0
        for i in range(1,len(nums)):
            if nums[i]!=nums [i-1 ]:
                temp+=1 
            answer += temp
        return  answer 


       



