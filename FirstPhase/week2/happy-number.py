class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()

        while n not in visited:
            visited.add(n)
            n=self.squereSum(n)

            if n == 1 :
                return True 
        return False 
        
    def squereSum(self , n: int ):
        Sum=0
        while n:
            d=n%10
            Sum = Sum+(d**2)
            n=n//10 
        return Sum 
       
       
            
             

            

        