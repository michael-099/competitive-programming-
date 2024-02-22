class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # the trick for this quesion is finding the mathimatical formula
        if sum(nums) % p == 0:
            return 0
        target = sum(nums) % p
        dic = {0: -1}
        n = len(nums)
        cur=0
        size = n
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            if dic.get((cur - target) % p) is not None:
                size = min(size, i - dic.get((cur - target) % p))
            dic[cur] = i
        return size if size < n else -1
