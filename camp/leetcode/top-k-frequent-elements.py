class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1
        pair=[]
        for key,value in dic.items():
            pair.append([value,key])
        pair.sort(reverse=True)
        res=[]
        for i in range(k):
            res.append(pair[i][1])
        return res
        
            
        