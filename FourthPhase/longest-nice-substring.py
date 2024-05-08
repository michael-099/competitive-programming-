class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        maxi = -1
        stri = ""
        for i in range (len(s)):
            substrings=s[i]
            for j in range (i+1,len(s)):
                substrings+=s[j]
                flag = True
                for k in substrings:
                    if k.isupper():
                        small = k.lower()
                    else:
                        small = k.upper()
                    if small not in substrings:
                        flag = False
                if flag and len(substrings) > maxi:
                    maxi = len(substrings)
                    stri = substrings

        return stri
        
