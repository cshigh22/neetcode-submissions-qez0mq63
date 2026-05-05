class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, c in enumerate(nums):
            diff = target - c
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[c] = i
        return []
            