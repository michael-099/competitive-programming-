class Solution:
    def countBits(self, n: int) -> List[int]:

        def count_ones(n,count):
            while n!=0:
                rem=n%2
                if rem==1:
                    count+=1
                n=n//2
            return count

        outPut=[]
        for i in range(n+1):
            outPut.append(count_ones(i,0))
        return outPut
        