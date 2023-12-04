class Solution:
    def kidsWithCandies(self, c: List[int], extra: int) -> List[bool]:
        arr=[]
        Max=max(c)
        for i in range(len(c)):
            if c[i]+extra>=Max:
                arr.append(True)
            elif c[i]+extra<Max :
                arr.append(False)
        return arr 
