class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_t = {}
        hashmap_s = {}

        for i in s:
            hashmap_s[i] = 1 + hashmap_s.get(i, 0)
        for i in t:
            hashmap_t[i] = 1 + hashmap_t.get(i, 0)

        return hashmap_s == hashmap_t