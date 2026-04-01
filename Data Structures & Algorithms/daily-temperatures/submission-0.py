class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[temp, index]
        res = [0] * len(temperatures)

        for i, c in enumerate(temperatures):
            while stack and c > stack[-1][1]:
                stackInd, stackT = stack.pop()
                res[stackInd] = i - stackInd

            stack.append([i, c])
        return res