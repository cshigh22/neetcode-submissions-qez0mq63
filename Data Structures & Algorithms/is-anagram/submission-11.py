class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}

        for i in s:
            hashmapS[i] = 1 + hashmapS.get(i, 0)

        for i in t:
            hashmapT[i] = 1 + hashmapT.get(i, 0)

        return hashmapS == hashmapT
