class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = []
        t_set = []
        for i in s:
            s_set.append(i)
        for i in t:
            t_set.append(i)
        s_set.sort()
        t_set.sort()
        return s_set == t_set