class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check=[]
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                check.append(j)
        # print (check)
        # print (right , left )
        for i in range(left,right+1):
            # print(left)
            if i not in check:
                return False

        return True 
