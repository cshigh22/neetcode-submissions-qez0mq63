class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for i in nums:
            if i - 1 not in nums:
                curr = 1
                while i + curr in s:
                    curr += 1
                res = max(res, curr)
        return res