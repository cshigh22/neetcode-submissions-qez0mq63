class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, c in enumerate(nums):
            difference = target - c
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[c] = i
            