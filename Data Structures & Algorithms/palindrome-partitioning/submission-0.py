class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def is_pal(sub):
            return sub == sub[::-1]

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            for j in range(i + 1, len(s) + 1):
                prefix = s[i:j]
                if is_pal(prefix):
                    part.append(prefix)
                    dfs(j)
                    part.pop()
        dfs(0)
        return res
    