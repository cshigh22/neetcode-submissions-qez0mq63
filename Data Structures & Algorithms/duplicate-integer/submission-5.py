class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for i in nums:
            dup.add(i)
        return len(dup) != len(nums)