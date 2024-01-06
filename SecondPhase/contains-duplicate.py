class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num=list(set(nums))
        print(num)
        return not(len(num)==len(nums))
        
        