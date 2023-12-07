class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output=""
        for i in range(len(s)):
           output+=s[indices.index(i)]
        return output
     
        

      