class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-1*num for num in nums]
        heapify(nums)
        res=0
        for i in range(k):
            res=heappop(nums)
        return -(res)
        