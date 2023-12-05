class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        start=0
        end=1
        arr=[]
        while end<len(nums):
            for i in range(nums[start]):
                arr.append(nums[end])
            start=start+2
            end=end+2
        return arr 

        