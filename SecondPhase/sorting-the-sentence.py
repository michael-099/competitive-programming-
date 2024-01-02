class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        s.sort(key=lambda x: x[-1])
        sentence =""
        for i in range(len(s)):
            sentence+=s[i][0:len(s[i])-1]+" "
        return sentence[:len(sentence)-1]
            

