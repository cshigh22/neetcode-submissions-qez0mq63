class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sort = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        
        for key, value in sort.items():
            freq[value].append(key)

        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
