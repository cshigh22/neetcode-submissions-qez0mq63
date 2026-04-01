class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = 0
        
        def dfs(r, c):
            if (r < 0 or r >= rowLen or c < 0 or c >= colLen or grid[r][c] == "0"):
                return 
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == "1":
                    dfs(r, c)
                    result += 1
        return result
            