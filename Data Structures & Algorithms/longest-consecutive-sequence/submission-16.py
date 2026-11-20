class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0

        for i in hashset:
            if i - 1 not in hashset:
                curr = 1
                while i + curr in hashset:
                    curr += 1
                res = max(res, curr)
        return res
