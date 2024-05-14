class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        initial=0
        for op in operations:
            if op=="--X" or op== "X--" :
                initial-=1
            else :
                initial +=1
        return initial

        