class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0]*(len(s)+1)
        for i in range(len(shifts)):
            if shifts[i][2]==1:
                prefix[shifts[i][0]]+=1
                prefix[shifts[i][1]+1]-=1
            else:
                prefix[shifts[i][0]]-=1
                prefix[shifts[i][1]+1]+=1

        prefix.pop()
        running_sum=0

        for i in range (len(prefix)):
            running_sum+=prefix[i]
            prefix[i]=running_sum

        alphabet=[chr(i) for i in range(ord("a"),ord("z")+1)]
        alpha={chr(i):i-ord("a") for i in range (ord("a"),ord("z")+1) }
        
        for i in range (len(prefix)):
            prefix[i]+=alpha[s[i]]


        string=""
        for i in range (len(prefix)):
            string=string+alphabet[prefix[i]%26]
        return string 
            
