class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # the soluttion is finding the next largest or equal to the target and return its index 
        left,right,current_largest=0,len(nums)-1,0
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                current_largest=mid
                right=mid-1
            else:
                left=mid+1
       
        return current_largest if left!=len(nums) else len(nums)



        