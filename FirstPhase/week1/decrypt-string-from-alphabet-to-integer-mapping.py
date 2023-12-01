class Solution:
    def freqAlphabets(self, s: str) -> str:
       dic={}
       alpha="abcdefghijklmnopqrstuvwxyz"
       for x in range(len(alpha)-1,-1,-1) :
           if x<9:
               dic[alpha[x]]=(f"{x+1}")
           else:
               dic[alpha[x]]=(f"{x+1}#")
       for key,value in dic.items():
           if value in s:
               s=s.replace(value,key)
       return s