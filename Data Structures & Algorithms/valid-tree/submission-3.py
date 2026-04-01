class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(n)}
        visited = set()

        for i, j in edges:
            hashmap[i].append(j)
            hashmap[j].append(i)

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for i in hashmap[node]:
                if i == parent:
                    continue
                if not dfs(i, node):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)
