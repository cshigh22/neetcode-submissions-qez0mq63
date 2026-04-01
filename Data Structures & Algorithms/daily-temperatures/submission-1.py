class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, c in enumerate(temperatures):
            while stack and c > stack[-1][1]:
                stackidx, stackT = stack.pop()
                res[stackidx] = i - stackidx
            stack.append([i, c])
        return res