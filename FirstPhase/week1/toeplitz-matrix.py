class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix)==1 or len(matrix[1])==1:
            return True 
        for i in range (len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False 
        return True 
         
         
         
         
         
         
         
         
         
         
         
         
         
        #     if matrix[i][i]!=first:
        #         return False 
        # return True 

        