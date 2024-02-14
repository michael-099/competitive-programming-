class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        remaining=k
        count=0
        Sum=0
        if remaining >numOnes:
             remaining=remaining-numOnes
             count+=numOnes
             Sum=Sum+numOnes
        elif remaining <= numOnes:
            count=count+remaining 
            Sum=Sum+remaining 
            return Sum
        if remaining >numZeros:
             remaining=remaining-numZeros
             count+=numZeros
        elif remaining <= numZeros:
            count=count+remaining
            return Sum 
        if remaining >numNegOnes:
             remaining=remaining-numNegOnes
             count+=numNegOnes
             Sum-=numNegOnes
        elif remaining <=numNegOnes:
            count=count+remaining
            Sum-=remaining
            return Sum
        return 0
        


        