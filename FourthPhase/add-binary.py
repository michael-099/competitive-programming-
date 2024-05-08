class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convertBack(num):
            binary = []
            if num==0:
                return "0"
            else:
                while num > 0:
                    binary.append(str(num % 2))
                    num = num // 2
                binary.reverse()
                print("binary",binary)
                return "".join(binary)
        
        def convert(bit):
            res=0
            for i in range(len(bit)-1,-1,-1):
                if bit[i]=="1":
                    res=res+(2**((len(bit)-1)-i))
            return res 
        print(convert(a),convert(b))
        return convertBack(convert(a)+convert(b))