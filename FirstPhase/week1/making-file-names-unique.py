class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        dic={}
        List=[]
        for i in names:
            if i in dic:
                while i+f"({dic[i]})" in dic:
                    dic[i]=dic[i]+1
                List.append(i+f"({dic[i]})")
                dic[i+f"({dic[i]})"]=1
                dic[i]=dic[i]+1
            else :
                dic[i]=1 
                List.append(i)
                
        return List 

        