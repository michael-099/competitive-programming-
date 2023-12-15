class Bitset:

    def __init__(self, size: int):
        self.bits=[0]*size
        self.f=[1]*size
        self.Count=0
        

    def fix(self, idx: int) -> None:
        if self.bits[idx]==0 :
            self.Count+=1
        self.bits[idx]=1
        self.f[idx]=0

    def unfix(self, idx: int) -> None:
        if self.bits[idx]==1 :
            self.Count-=1

        self.bits[idx]=0
        self.f[idx]=1
        

    def flip(self) -> None:
        temp=self.bits
        self.bits=self.f
        self.f=temp
        self.Count=len(self.bits)-self.Count
       
        

    def all(self) -> bool:
        if self.Count == len(self.bits):
            return True 
        return False
        
        

    def one(self) -> bool:
        if self.Count >0 :
            return True 
        return False 
        

    def count(self) -> int:
        # print( self.bits.count(1))
        return self.Count 
      
        

    def toString(self) -> str:
        count=""
        # print(self.bits)
        for i in range(len(self.bits)):
            count=count+str(self.bits[i])
        return count
            
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()