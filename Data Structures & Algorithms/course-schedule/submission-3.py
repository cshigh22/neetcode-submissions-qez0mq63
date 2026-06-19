class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        preMap = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)
            for i in preMap[crs]:
                if not dfs(i):
                    return False
            visit.remove(crs)
            
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True