class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res= []
        for i in range(len(boxes)):
            count=0
            for j in range(len(boxes)-1,-1,-1 ):
                if boxes[j]=="1":
                    count=count+abs(j-i)
            res.append(count)
        return res
                
        