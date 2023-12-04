class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={x:i for i,x in enumerate(order) }
        print(dic)
        arr=[]
        for i in range(len(words)):
            num=[]
            for j in range(len(words[i])):
               num.append(dic[words[i][j]])
            arr.append(num)
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return False 
        return True 

       