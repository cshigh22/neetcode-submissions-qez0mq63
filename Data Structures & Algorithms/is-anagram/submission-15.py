class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}

        for i in s:
            hashmap_s[i] = hashmap_s.get(i, 0) + 1
        for i in t:
            hashmap_t[i] = hashmap_t.get(i, 0) + 1

        return hashmap_s == hashmap_t