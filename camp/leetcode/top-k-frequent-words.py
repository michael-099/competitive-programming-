class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic={}
        for word in words:
            dic[word]=dic.get(word,0)+1
        pair=[]
        for key,value in dic.items():
            pair.append([key,value])
        # pair.sort(reverse=True)
        pair.sort(key=lambda x:(-x[1],x[0]))
        return [p[0] for p in pair[:k]]
       