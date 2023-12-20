class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=""
        for digit in digits:
            number+=str(digit)
        number=int( number)+1
        number=str(number)
        output = [int(i) for i in number]
        return output
        