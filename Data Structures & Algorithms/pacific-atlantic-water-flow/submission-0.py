class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen = len(heights)
        colLen = len(heights[0])
        pacific = set()
        atlantic = set()
        res = []
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visit, prev_height):
            if (r < 0 or r == rowLen or
                c < 0 or c == colLen or (r, c) in visit
                or heights[r][c] < prev_height):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])  
            dfs(r, c + 1, visit, heights[r][c]) 
            dfs(r, c - 1, visit, heights[r][c])


        for c in range(colLen):
            dfs(0, c, pacific, heights[0][c])
            dfs(rowLen - 1, c, atlantic, heights[rowLen - 1][c])
            
        for r in range(rowLen):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, colLen - 1, atlantic, heights[r][colLen - 1])

        res = []
        for r in range(rowLen):
            for c in range(colLen):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
