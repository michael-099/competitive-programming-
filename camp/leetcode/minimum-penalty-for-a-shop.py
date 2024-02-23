class Solution:
    def bestClosingTime(self, customers: str) -> int:
        bit=[]
        for i in range(len(customers)):
            if customers[i] =='Y':
                bit.append(0)
            else:
                bit.append(1)
        time=len(customers)
        min_penalty=sum(bit)
        penalty=sum(bit)
        print(penalty)
        for i in range (len(bit)-1,-1,-1):
            if bit[i]==0:
                bit[i]+=1
                penalty+=1
            else:
                bit[i]-=1
                penalty-=1
                if penalty<=min_penalty:
                    min_penalty=penalty 
                    time=i 
        return time

            



        