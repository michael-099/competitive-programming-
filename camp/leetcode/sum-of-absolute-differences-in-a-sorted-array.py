class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        suffix = [0] * (len(nums) + 2)
        prefix_running_sum = 0
        suffix_running_sum = 0
        summation = 0
        summation_arr = []
        
        for i in range(len(nums)):
            prefix_running_sum += nums[i]
            prefix.append(prefix_running_sum)
        prefix.append(0)

        for i in range(len(nums) - 1, -1, -1):
            suffix_running_sum += nums[i]
            suffix[i + 1] = suffix_running_sum
       
        for i in range(len(nums)):
            summation = abs(
                ((i * nums[i]) - prefix[i])
                + (suffix[i + 2] - (len(nums) - 1 - i) * nums[i])
            )
            summation_arr.append(summation)
        return summation_arr
