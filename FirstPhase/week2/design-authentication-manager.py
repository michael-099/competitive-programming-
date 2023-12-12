class AuthenticationManager:   
    
   
    def __init__(self, timeToLive: int):
        self.dictionary={"timeToLive":0 ,"generate":{}}
        self.dictionary["timeToLive"]=timeToLive
        # print(self.dictionary["generate"])


        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dictionary["generate"][tokenId]=currentTime+self.dictionary["timeToLive"]
        # print(self.dictionary["generate"])

        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dictionary["generate"] :
            if  self.dictionary["generate"][tokenId]>currentTime:
                self.dictionary["generate"][tokenId]=currentTime+self.dictionary["timeToLive"]

        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for token,time in (self.dictionary["generate"]).items():
            # print (self.dictionary["generate"])
            if currentTime<time:
                count=count+1 
        return count

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)