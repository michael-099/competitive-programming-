class Solution:
    def minOperations(self, s: str) -> int:
        count1 = count2 = 0
        start = s[0]
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "1":
                count1 += 1
            elif i % 2 != 0 and s[i] == "0":
                count1 += 1

        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "0":
                count2 += 1
            elif i % 2 != 0 and s[i] == "1":
                count2 += 1
        return min(count1, count2)
