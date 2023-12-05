class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output=[]
        for string in range(len(words)):
            row1,row2,row3=0,0,0
            for index in range(len(words[string])):
                if  words[string][index].lower() in "qwertyuiop":
                    row1=row1+1
                if words[string][index].lower() in "asdfghjkl":
                    row2=row2+1
                if words[string][index].lower() in "zxcvbnm":
                    row3=row3+1
            if row1==len(words[string]) or row2==len(words[string]) or row3==len(words[string]):
                output.append(words[string])
        return output
            
        