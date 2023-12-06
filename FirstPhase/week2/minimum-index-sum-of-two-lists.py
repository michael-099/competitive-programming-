class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic={}
        for index in range  (len(list1)):
            if list1[index] in list2 :
                dic[list1[index]]=index+list2.index(list1[index])
                
        common_string=[]
        min_sum=min(dic.values())

        for strings in dic:
            if dic[strings]==min_sum:
                common_string.append(strings)
        
        return common_string



        