class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        arranged=[]
        for number in nums:
            if number>=0:
                positive.append(number)
            else :
                negative.append(number)
        
        for i in range(len(positive)):
            arranged.append(positive[i])
            arranged.append(negative[i])
        
        return arranged 

        