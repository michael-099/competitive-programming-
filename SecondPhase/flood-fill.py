class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        img = copy.deepcopy(image)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        """directions that we are allowed to go """
        visited = [[False for i in range(len(image[0]))] for i in range(len(image))]
        """matrix to keep track of visited node (cell)"""

        def isbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        """this function checkes if it goes out of bound as we go to a certain direction"""
        
        def dfs(image, visited, row, col):
            visited[row][col] = True
            for direction in directions:
               
                " making each of the visited node true starting from the starting(image[sr][sc]) node"
                new_row = row + direction[0]
                new_col = col + direction[1]
                """we will have new_row and new_col by moving using a certain direction 
                and this new image[new_row][new_col] needs to be checked if it is in bound
                this variables get overridden as the loop continues so they are stored temporarily 
                this helps to handle the backtracking"""
                
                if (
                    isbound(new_row, new_col)
                    and not visited[new_row][new_col]
                    and image[new_row][new_col] == image[row][col]
                ):
                    img[new_row][new_col] = color
                    dfs(image, visited, new_row, new_col)

                """we check if the node is not visited and also in bound then we check if the 
                new node(cell) that we are at is similar with the previous one and if all those
                3 conditions are met we will continue our dfs to it and change the 
                matrix value and we are going to return  the updated matrix"""

        dfs(image, visited, sr, sc)
        img[sr][sc]=color
        return img
