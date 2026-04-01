class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        COLS = len(matrix[0])
        ROWS = len(matrix)

        COL = [False] * COLS
        ROW = [False] * ROWS

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    ROW[i] = True
                    COL[j] = True

        for i in range(ROWS):
            for j in range(COLS):
                if ROW[i] or COL[j]:
                    matrix[i][j] = 0
        