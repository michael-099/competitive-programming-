class Solution:
    def largestGoodInteger(self, num: str) -> str:
        start=0 
        end=2 
        string=""
        arr=[""]
        while end<len(num):
            if(num[end]==num[start]==num[start+1]):
                arr.append(string +num[end]+num[start]+num[start+1])
            start=start+1 
            end=end+1 
        return max(arr)
        