class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visited = [False] * n
        res = 0
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node):
            for i in adj[node]:
                if not visited[i]:
                    visited[i] = True
                    dfs(i)
            
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1

        return res