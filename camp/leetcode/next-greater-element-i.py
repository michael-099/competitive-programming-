class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stack=[]
        output=[]
        for num in nums2:
            while  stack and stack[-1]<num:
                dic[stack.pop()]=num
            stack.append(num)
        for num in nums1:
            output.append(dic.get(num ,-1))
        return output
