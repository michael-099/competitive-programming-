class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        perimeter = 0

        def check(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def chakeLand(row, col):
            return grid[row][col] == 1

        def findLand(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return [i, j]
        

        land = findLand(grid)
       
        row, col = land[0], land[1]

        def dfs(grid, visited, row, col):
            nonlocal perimeter
            visited[row][col] = True
            curr_per = 0
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if (
                    check(new_row, new_col)
                    and chakeLand(new_row, new_col) 
                    and visited[new_row][new_col] == False
                ):
                    dfs(grid, visited, new_row, new_col)
                if not check(new_row, new_col) or not chakeLand(new_row, new_col):
                    curr_per += 1
                    perimeter += 1

        dfs(grid, visited, row, col)
        return perimeter
