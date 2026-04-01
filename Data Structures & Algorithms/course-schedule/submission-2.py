class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        hashmap = {i:[] for i in range(numCourses)}

        for i, j in prerequisites:
            hashmap[i].append(j)

        def dfs(node):
            if node in path:
                return False
            if hashmap[node] == []:
                return True

            path.add(node)

            for prereq in hashmap[node]:
                if not dfs(prereq):
                    return False
                
            path.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            