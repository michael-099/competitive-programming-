class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output=[]
        Sum=0
        for num in  nums:
            if num%2==0:
                Sum=Sum+num

        for val,index in (queries):
            if nums[index]%2==0:
                Sum=Sum-nums[index]
            nums[index]+=val
            if nums[index]%2==0:
                Sum=Sum+nums[index]
            # print(nums)
            output.append(Sum)

        return output


        