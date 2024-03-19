class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half):
            # write your code here
            left,right=0,0
            merged=[]
            while left<len(left_half)and right<len(right_half):
                if left_half[left]<right_half[right]:
                    merged.append(left_half[left])
                    left+=1 
                else:
                    merged.append(right_half[right])
                    right+=1
            merged.extend(left_half[left:len(left_half)])
            merged.extend (right_half[right:len(right_half)])
            return merged 

        def mergeSort(low,high,nums):
            if low==high:
                return [nums[low]]
            mid=(low+high)//2
            left=mergeSort(low,mid,nums)
            right=mergeSort(mid+1,high,nums)
            
            return merge(left,right)

        return mergeSort(0,len(nums)-1,nums)