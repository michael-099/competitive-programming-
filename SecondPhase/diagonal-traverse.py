class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        diagonal = {}
        diagonal2 = {}
        output = []

        for row in range(rows):
            for col in range(cols):
                if row + col not in diagonal:
                    diagonal[row + col] = [mat[row][col]]
                else:
                    diagonal[row + col].append(mat[row][col])

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row + col not in diagonal2:
                    diagonal2[row + col] = [mat[row][col]]
                else:
                    diagonal2[row + col].append(mat[row][col])

        output = []
        for i in range(cols + rows - 1):
            if i % 2 == 0:
                output = output + diagonal2[i]

            else:
                output = output + diagonal[i]

        return output
