class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visit = [0] * numCourses
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if visit[crs] == 1:
                return False
            if visit[crs] == 2:
                return True
            
            visit[crs] = 1

            for i in preMap[crs]:
                if not dfs(i):
                    return False
            
            visit[crs] = 2
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            