class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        def ispal(s):
            start=0
            end=len(s)-1
            while end>start:
                if s[end]!=s[start]:
                    return False
                end-=1
                start+=1
            return True
        def maptonum(s):
            alphabet={}
            for i in range(26):
                alphabet[chr(97 + i)] = i + 1
            arr = [alphabet[i] for i in s]
            return arr
        if len(palindrome) == 1:
                return ""
        string = ""  
        nums=maptonum(palindrome)
        for i in range(len(nums)):
            if i==len(nums)-1:
                nums[i]+=1
            if nums[i] > 1:
                if nums[i]==26:
                    nums[i]=1
                    break
                temp=nums[i]
                nums[i] = 1
                if ispal(nums):
                    nums[i]=temp
                else:
                    break
            

        for i in nums:
            string = string + chr(96 + i)
        return string
