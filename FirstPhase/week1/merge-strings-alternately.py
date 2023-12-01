class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output=""
        n=min(len(word1),len(word2))
        for i in range( n):
            output+=word1[i]
            output+=word2[i]
        if len(word1)>len(word2):
            for i in range(len(word2),len(word1)):
                output+=word1[i]
        if len(word2)>len(word1):
            for i in range(len(word1),len(word2)):
                output+=word2[i]
        return output 
        

        