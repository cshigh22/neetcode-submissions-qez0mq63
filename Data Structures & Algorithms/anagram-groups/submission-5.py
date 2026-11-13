class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            sorted_s = "".join(sorted(i))
            if sorted_s not in hashmap:
                hashmap[sorted_s] = []
            hashmap[sorted_s].append(i)
        return list(hashmap.values())
            
        
        # hashmap = defaultdict(list)

        # for i in strs:
        #     sorted_s = "".join(sorted(i))
        #     hashmap[sorted_s].append(i)
        # return list(hashmap.values())