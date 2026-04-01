class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            s.add(i)
        res = 0

        for i in nums:
            if i - 1 not in s:
                cur = 1
            
                while i + cur in s:
                    cur += 1
                
                res = max(res, cur)

        return res