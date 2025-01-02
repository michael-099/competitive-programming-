class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        voul={"a","e","i","o","u"}
        res=[]
        word=[0]
        for i in range(len(words)):
            if words[i][0] in voul and words[i][-1] in voul:
                val=1+word[-1] if word else 1
                word.append(val)
            else:
                val=0+word[-1] if word else 0
                word.append(val)
        print(word)
        
        for start,end in queries:
            res.append(word[end+1]-word[start])
        return res

