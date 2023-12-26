class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in range(len(arr2)):
            for  j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    a.append(arr1[j])
        for i in range(len(arr1)):
            if arr1[i] not in a:
                b.append(arr1[i])
        b.sort()
        return a+b
                

            

            
        