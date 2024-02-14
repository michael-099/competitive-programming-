class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        remaining=k
        Sum=0
        if remaining >numOnes:
             remaining=remaining-numOnes
             Sum=Sum+numOnes
        elif remaining <= numOnes:
            Sum=Sum+remaining 
            return Sum
        if remaining >numZeros:
             remaining=remaining-numZeros
        elif remaining <= numZeros:
            return Sum 
        if remaining >numNegOnes:
             remaining=remaining-numNegOnes
             Sum-=numNegOnes
        elif remaining <=numNegOnes:
            Sum-=remaining
            return Sum
        return 0
        


        