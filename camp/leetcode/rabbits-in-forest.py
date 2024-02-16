class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic={}
        rabbits=0
        for color in answers:
            if color in dic and dic[color]>0:
                dic[color]-=1        
            elif color in dic and dic[color]==0:
                dic[color]=color
                rabbits+=dic[color]+1
            elif color not in dic:
                dic[color]=color
                rabbits += dic[color]+1
        return rabbits
            

    
        