class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq=[0]*(len(nums))
        max_sum=0 
        running_sum=0
        res=0
        modulo= 10**9 + 7
        output=[0]*len(nums)
        for i in range(len(requests)): 
            freq[requests[i][0]]+=1
            if requests[i][1]!= len(nums)-1:
                freq[requests[i][1]+1]-=1
        for i in range(len(freq)):
            running_sum+=freq[i]
            freq[i]=running_sum
        freq.sort()
        nums.sort()
        for i in range(len(nums)):
            res=res+(freq[i]*nums[i])
        return res % modulo  
      
        

        