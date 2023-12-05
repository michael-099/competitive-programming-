class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        max_length=0
        for char in s:
            max_length=max(len(char),max_length)
        
        words_in_column=[""]*max_length

        for string in range(len(s)):
            for string_index in range(max_length):
                if len(s[string])-1<string_index:
                   words_in_column[string_index]= words_in_column[string_index]+" "
                else:
                    words_in_column[string_index]= words_in_column[string_index]+(s[string][string_index])
        words_in_column=[string.rstrip() for string in words_in_column]

                     
        return words_in_column


        