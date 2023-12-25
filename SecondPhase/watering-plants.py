class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count=0
        o=capacity
        i=0
        while i<len(plants):
            if capacity-plants[i]>=0:
                capacity=capacity-plants[i]
                count=count+1
                i+=1
            else:
                count=count+2*i
                capacity=o
        return count


                
        

        
        