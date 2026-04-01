class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}

        for i, c in enumerate(nums):
            difference = target - c

            if difference in l:
                return [l[difference], i]  
            l[c] = i

