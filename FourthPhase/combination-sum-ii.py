class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(i,arr,target):
            if target==0:
                res.append(arr[:])
                return
            if target<=0:
                return
            
            prev=-1
            for candidate in range(i,len(candidates)):
                if prev != candidates[candidate]:
                   
                    arr.append(candidates[candidate])
                    backtrack(candidate+1,arr,target-candidates[candidate])
                    arr.pop()
                    prev=candidates[candidate]
            
        res=[]
        backtrack(0,[],target)
        return res
        