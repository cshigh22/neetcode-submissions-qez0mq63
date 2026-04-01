class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, c in enumerate(nums):
            complement = target - c
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[c] = i
