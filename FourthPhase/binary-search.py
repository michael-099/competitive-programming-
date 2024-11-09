class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right=len(nums)-1
        left=0
        
        while right>=left:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]==target:
                return mid 
        return -1 
            


        