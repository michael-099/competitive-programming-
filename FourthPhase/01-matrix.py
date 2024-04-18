
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        rows, cols = len(mat), len(mat[0])
        res = [[-1 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    res[i][j] = 0

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and res[new_row][new_col] == -1:
                    res[new_row][new_col] = res[row][col] + 1
                    queue.append((new_row, new_col))

        return res
