class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True 

        path = set()
        hashmap = {i:[] for i in range(n)}

        for i, j in edges:
            hashmap[i].append(j)
            hashmap[j].append(i)
            
        def dfs(node, par):
            if node in path:
                return False

            path.add(node)

            for j in hashmap[node]:
                if j == par:
                    continue
                if not dfs(j, node):
                    return False
            return True
                
        return dfs(0, -1) and n == len(path)