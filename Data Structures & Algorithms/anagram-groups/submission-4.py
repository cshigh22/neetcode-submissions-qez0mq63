class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            sorted_s = "".join(sorted(i))
            hashmap[sorted_s].append(i)
        return list(hashmap.values())