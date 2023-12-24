class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows=len(mat)
        cols=len(mat[0])
        diagonals={}
        diagonals2={}
        intersection=0
        
        for row in range (rows):
            for col in range (cols):
                if row-col in diagonals:
                    diagonals[row-col].append(mat[row][col])
                else:
                    diagonals[row-col]=[mat[row][col]]
                if row+col in diagonals2:
                    diagonals2[row+col].append(mat[row][col])

                else:
                    diagonals2[row+col]=[mat[row][col]]
        
        if col%2==0:
            intersection=mat[rows//2][cols//2]
            
        diagonal_sum= (sum(diagonals[0])+sum(diagonals2[rows-1]))-intersection
        return diagonal_sum
       

                
        