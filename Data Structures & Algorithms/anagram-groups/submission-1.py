class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            sorted_i = "".join(sorted(i))
            hashmap[sorted_i].append(i)

        return list(hashmap.values())