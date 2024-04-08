class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        time, fresh = 0, 0
        queue = deque()

        def check(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i, j])
                    visited[i][j]==True
       

        while queue and  fresh>0:
            print(queue)
            for _ in range(len(queue)):
                row,col = queue.popleft()
                

              
                

                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if (
                        check(new_row,new_col)
                        and grid[new_row][new_col] == 1
                        and not visited[new_row][new_col]
                    ):  
                        visited[new_row][new_col] = True
                        queue.append([new_row,new_col])
                        fresh -= 1

            time += 1
            print(fresh)
        return -1 if fresh else time
