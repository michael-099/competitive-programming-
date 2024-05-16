class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(i,arr):
            if len(arr) == k:
                res.append(arr[:])
                return
            
            
            for j in range (i,n+1):
                arr.append(j)
                backtrack(j+1,arr)
                arr.pop()

        res=[]
        backtrack(1,[])
        return res


            


            
