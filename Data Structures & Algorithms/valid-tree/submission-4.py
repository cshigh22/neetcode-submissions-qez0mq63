class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visit = set()
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for nei in adj[i]:
                dfs(nei)
        dfs(0)
        return len(visit) == n