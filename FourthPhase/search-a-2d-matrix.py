class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        right, left = len(matrix)-1, 0

        def checkRow(row, target):
            return True if row[0] <= target and row[len(row) - 1] >= target else False

        target_row = []
        while right >= left:
            print(right,left)
            mid = (left + right) // 2
            print(mid)
            if checkRow(matrix[mid], target):
                target_row = matrix[mid]
                break
            else:
                if matrix[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        left,right=0,len(target_row)-1

        while right>= left:
            mid=(left+right)//2
            if target_row[mid]==target:
                return True
            elif target_row[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False