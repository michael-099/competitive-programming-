class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        left_pr = []
        right_pr = [1] * (len(nums))
        running_pr = 1
        for i in range(len(nums)):
            running_pr = running_pr * nums[i]
            left_pr.append(running_pr)

        running_pr = 1
        for i in range(len(nums) - 1, -1, -1):
            running_pr = running_pr * nums[i]
            right_pr[i] = running_pr

        for i in range(0, len(left_pr)):
            if i == 0:
                arr.append(right_pr[i + 1])
            elif i == len(nums) - 1:
                arr.append(left_pr[i - 1])
            else:
                arr.append(right_pr[i + 1] * left_pr[i - 1])
        return arr
