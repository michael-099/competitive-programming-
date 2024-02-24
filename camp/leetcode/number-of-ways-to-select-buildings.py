class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros_prefix, ones_prefix, zeros_suffix, ones_suffix = (
            [],
            [],
            [0] * len(s),
            [0] * len(s),
        )
        zeros, ones = 0, 0
        bldgs = 0
        for i in range(len(s)):
            if s[i] == "1":
                ones = ones + 1
            else:
                zeros = zeros + 1
            ones_prefix.append(ones)
            zeros_prefix.append(zeros)
        zeros, ones = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1
            ones_suffix[i] = ones
            zeros_suffix[i] = zeros
        # print(zeros_prefix, zeros_suffix, ones_prefix, ones_suffix)

        for i in range(len(s)):
            if s[i] == "1":
                
                bldgs = bldgs + (zeros_prefix[i] * zeros_suffix[i])
            else:
                bldgs = bldgs + (ones_prefix[i] * ones_suffix[i])
        return bldgs
