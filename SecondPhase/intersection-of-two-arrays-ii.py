class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary1={}
        dictionary2={}
        store=[]
       
        for i in nums1:
            if i in dictionary1:
                dictionary1[i]+=1
            else:
                dictionary1[i]=1   
        
        for i in nums2:
            if i in dictionary2:
                dictionary2[i]+=1
            else:
                dictionary2[i]=1  
        for key,value in dictionary1.items():
            arr=[]
            if key in dictionary2:
                arr=[key]*min(dictionary1[key],dictionary2[key])
            store=store+arr
        
        return store
