class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low,high=0,len(nums)-1

        while high>=low:
            mid=(high+low)//2
            if nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        start=low
        low,high=0,len(nums)-1
        while high>=low:
            mid=(high+low)//2
            if nums[mid]<=target:
                low=mid+1
            else:
                high=mid-1
        end=high
        return [start,end] if end>=start else [-1,-1]


        

    
        
            

        