class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set()
        for i in nums:
            s.add(i)
        res = 1
        cur = 1
        so = sorted(s)

        for i in range(1, len(so)):
            if so[i] == 1 + so[i-1]:
                cur += 1
            else:
                cur = 1
            res = max(res, cur)

        return res