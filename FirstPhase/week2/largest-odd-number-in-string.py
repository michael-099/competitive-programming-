class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if (int(num[i])%2!=0):
                return num
            else:
                num=num[0:len(num)-1]
        return num



        