class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        running_sum, count = 0, 0
        dic = {0:1}

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1


        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - k in dic:
                count += dic[running_sum - k]
            dic[running_sum] = dic.get(running_sum, 0) + 1
            
        return count
