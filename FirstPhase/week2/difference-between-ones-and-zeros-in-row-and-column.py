class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        oneRow=[sum(x) for x in grid]
        oneCol=[]
       
        for i in range (len(grid[0])):
            count=0
            for j in range(len(grid)):
                if grid[j][i]==1:
                    count=count+1
            oneCol.append(count)

        diff=[]
        for i in range (len(oneRow)):
            arr=[]
            for j in range (len(oneCol)):
                d=(oneRow[i])+(oneCol[j])-(len(oneRow)-oneRow[i])-(len(oneCol)-oneCol[j])
                arr.append(d)
            diff.append(arr)
            
        return diff 



                



        