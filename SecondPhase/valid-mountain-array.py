class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)< 3 or  arr[0]>=arr[1]:
            return False
        Flag = True
        alter = 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            if arr[i] > arr[i + 1]:
                alter = i+1
                break
        for i in range(alter, len(arr)-1):
            if arr[i] == arr[i + 1]:
                return False
            if arr[i] < arr[i + 1]:
                return False
                
        return Flag
