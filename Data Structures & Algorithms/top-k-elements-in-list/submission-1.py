class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        res = []
        for key, value in hashmap.items():
            res.append([value, key])
        res.sort()

        result = []
        while len(result) < k:
            result.append(res.pop()[1])
        return result
            

        
        