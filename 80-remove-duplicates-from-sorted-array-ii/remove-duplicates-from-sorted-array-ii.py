class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        count=1

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                count+=1
                continue
            num=nums[i]
            if count == 1 :
                nums[k]=num
                k += 1
                count = 1

            if count >= 2:  
                nums[k],nums[k+1]=num,num
                k += 2
                count = 1
        if count == 1 :
                nums[k]=nums[-1]
                k += 1
               

        elif count >= 2:  
                nums[k],nums[k+1]=nums[-1],nums[-1]
                k += 2

        while len(nums)!= k:
            nums.pop()
                
            


       




           
        
            

            
            



        
            

        
        