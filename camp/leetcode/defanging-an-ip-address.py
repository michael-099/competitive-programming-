class Solution:
    def defangIPaddr(self, address: str) -> str:
        m=address.split(".")
        print(m)
        s=""
        for i in range(len(m)):
            s=s+m[i]
            s=s+"[.]"
        return s[:-3]
        