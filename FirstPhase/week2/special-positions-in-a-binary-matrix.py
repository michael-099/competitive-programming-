class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0 
        col=[0]*len(mat[0])
        row=[0]*len(mat)

        for i in range(len(mat)):
            for j in range (len(mat[i])):
                if mat[i][j]==1:
                    row[i]+=1
        for i in range(len(mat[0])):
            for j in range (len(mat)):
                      
                if mat[j][i]==1:
                    col[i]+=1
                  
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==1 and row[i]==1 and col[j]==1:
                    count=count+1
                
        return count 
        