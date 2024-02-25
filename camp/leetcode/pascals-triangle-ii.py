class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle=[]
        if rowIndex==0:
            return [1]
        for i in range(1,rowIndex+1):
            triangle.append([0]*(i+1))
        for row in triangle :
            row[0]=1
            row[len(row)-1]=1
        for row  in range(len(triangle)):
            for val  in range(len(triangle[row])):
                if triangle [row][val]==0:
                    triangle[row][val]=triangle[row-1][val]+triangle[row-1][val-1]   
        print (triangle)              
        return triangle[-1]
        