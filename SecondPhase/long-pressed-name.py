class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left = 0
        right = 0
        while len(typed) > right:
            if len(name) > left and name[left] == typed[right]:
                left += 1
                right += 1
            elif typed[right - 1] == typed[right] and right > 0:
                right += 1
            else:
                return False
        return left == len(name)
