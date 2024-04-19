class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])

        def check(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(board, row, col):

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited = set()
            visited.add((row, col))

            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if (
                    check(new_row, new_col)
                    and (new_row, new_col) not in visited
                    and board[new_row][new_col] == "O"
                ):
                    board[new_row][new_col] = "M"
                    dfs(board,new_row, new_col)

        for i in range(row):
            for j in range(col):
                if (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1) and board[i][j] == "O":
    
                    board[i][j] = "M"
                    dfs(board, i, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(row):
            for j in range(col):
                if board[i][j] == "M":
                    board[i][j] = "O"
