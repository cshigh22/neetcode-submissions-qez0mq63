class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in nums:
                if i not in path:
                    path.append(i)
                    dfs()
                    path.pop()

        dfs()
        return res