class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum = 0
        count = 0
        dic = {0: 1}

        for i in range(len(nums)):
            running_sum+=nums[i]
            rem=running_sum % k 
            if rem<0:
                rem+=k
            if rem in dic:
                count = count + dic[rem]
            dic[rem] = dic.get(rem, 0) + 1

        return count
