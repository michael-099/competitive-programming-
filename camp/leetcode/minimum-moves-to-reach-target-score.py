class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        """
        to use greedy in this question we need to keep in mind that greedy takes the current
        optimal choice with out considering the preivious and the future so how can we choose
        thecurrent optimal one ? so we have to know the right time to multiply our current value
        thats where we should get greedy we muliply by the time we can get the maximum out of it
        starting point= 1
        question : how can we use our doubles efficently
        """
        count = 0
        while target > 1:
            if maxDoubles==0:
                count+=target-1
                return count
            if target % 2 != 0 :
                target = target - 1
                count += 1
            elif target % 2 == 0 and maxDoubles > 0:
                target = target // 2
                count += 1
                maxDoubles -= 1
        return count
