class Solution:
    def smallestNumber(self, num: int) -> int:

        def nextNonZero(self,num):
            for i in range(len(nums)):
                if nums[i]!=0:
                    return i

        num = str(num)
        if len(num)==1:
            return int(num)
        negative = True if num[0] == "-" else False
        nums = []
        for i in num:
            if i != "-":
                nums.append(int(i))

        if not negative:
            nums.sort()

            if nums[0] == 0:
                i=nextNonZero(self,num)
                nums[0], nums[i] = nums[i], nums[0]
            nums = [str(i) for i in nums]
            min_ = "".join(nums)
            

        else:
            nums.sort(reverse=True)
            nums = [str(i) for i in nums]
            min_ = "".join(nums) 
    

        return int(min_) if not negative else int(min_)*-1
