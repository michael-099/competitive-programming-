class OrderedStream:

    def __init__(self, n: int):
        self.n=n
        self.pointer=0
        self.arr=[""]*(n+1)
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1]=value
        temp=[]
        while self.arr[self.pointer] != "" and self.pointer<self.n:
            temp.append(self.arr[self.pointer])
            self.pointer+=1
        return temp

            

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)