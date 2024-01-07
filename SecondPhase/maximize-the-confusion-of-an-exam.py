class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        end,start,max_fre,count,res=0,0,0,0,0
        dic={}

        for end in range (len(answerKey)):
            dic[answerKey[end]]=dic.get(answerKey[end],0)+1
            count=count+1 
            max_fre=max(max_fre,dic[answerKey[end]])

            while (end-start+1)-max_fre>k:
                dic[answerKey[start]]-=1
                start=start+1 
                count=count-1 
            res=max(res,count )
        return res 


        