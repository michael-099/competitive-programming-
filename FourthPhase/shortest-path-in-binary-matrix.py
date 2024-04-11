
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or not grid or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
            return -1
        
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
            [1, 1],
            [-1, 1],
            [1, -1],
            [-1, -1],
        ]
        
        queue = deque()
        queue.append([0, 0])
        visited = set()
        visited.add((0, 0))
        length = 1  # Start from 1 because we're counting the initial cell as well

        def check(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return length  # Return length + 1 as we're counting the current cell
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if (
                        check(new_row, new_col)
                        and (new_row, new_col) not in visited
                        and grid[new_row][new_col] == 0
                    ):
                        visited.add((new_row, new_col))
                        queue.append([new_row, new_col])

            length += 1

        return -1
