class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = set()
        for i in nums:
            size.add(i)
        return len(nums) != len(size)