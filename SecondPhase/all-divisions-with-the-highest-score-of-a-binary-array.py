class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
       
        zero_count,one_count=0,sum(nums)
        score=[0]*(len(nums)+1)
        
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
            score[i+1]=zero_count
        
        score[0]=one_count
        for i in range(len(nums)):
            if nums[i]==1:
                one_count-=1
            score[i+1]+=one_count
            
        Max=max(score)
        output=[]
        for i in range (len(score)):
            if score[i] == Max:
                output.append (i)
        return output




