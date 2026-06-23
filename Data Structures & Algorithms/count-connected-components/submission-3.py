class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs approach
        # adj = {i: [] for i in range(n)}
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        # visit = set()
        # res = 0

        # def dfs(node):
        #     visit.add(node)
        #     for nei in adj[node]:
        #         if nei not in visit:
        #             dfs(nei)

        # for i in range(n):
        #     if i not in visit:
        #         dfs(i)
        #         res += 1
        # return res

        # union find approach
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res