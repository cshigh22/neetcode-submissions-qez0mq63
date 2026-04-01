class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hashset = set()
        row = len(board)
        col = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or c >= col or r >= row 
            or word[i] != board[r][c] or (r, c) in hashset):
                return False
            hashset.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                  dfs(r - 1, c, i + 1) or
                  dfs(r, c + 1, i + 1) or 
                  dfs(r, c - 1, i + 1))
            hashset.remove((r, c))
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False