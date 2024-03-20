class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low,high=0,len(letters)-1
        index=0
        while high>low:
            mid=(low+high)//2
            print(low,mid,high)
            if letters[mid]>target:
                high=mid
                
            elif letters[mid]<=target:
                low=mid+1
        return letters[low] if letters[low]>target else letters[0]


            

        

        