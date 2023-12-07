class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        larger=[]
        smaller =[]
        equal=[]
        for number in nums:
            if number>pivot:
                larger.append (number)
            elif number==pivot:
                equal.append(number)
            else:
                smaller.append(number)
        return smaller+equal+larger


        