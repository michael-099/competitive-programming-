class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled=[]
        for numbers in range(n):
            shuffled.append(nums[numbers])
            shuffled.append(nums[numbers+n])
        return  shuffled
        