class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        elements=[]
        for i in nums:
            dic[i]=dic.get(i,0)+1

        for key in dic:
            appearance= (len(nums)//3)+1 
            if (appearance)<=dic[key]:
                elements.append(key)
        return elements 

        