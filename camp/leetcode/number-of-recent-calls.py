class RecentCounter:

    def __init__(self):
        self.queue=[]
        self.headIndex=0
        

    def ping(self, t: int) -> int:
        self.queue.append([t-3000,t])
        while self.queue[self.headIndex][1]<self.queue[-1][0]:
            self.headIndex+=1
        return len(self.queue)-self.headIndex
        

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)