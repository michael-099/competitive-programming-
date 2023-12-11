class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        percent=len(arr)//4
        dic={}
        Max=0
        for i in arr:
            dic[i]=dic.get(i,0)+1
        for key,value  in dic.items():
            Max=max(Max,value)
        for key ,value in dic.items():
            if value==Max:
                return key
            
        return 0
        