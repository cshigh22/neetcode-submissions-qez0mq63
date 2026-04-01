class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, c in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                count = c + nums[left] + nums[right]

                if count > 0:
                    right -= 1
                elif count < 0:
                    left += 1
                else:
                    res.append([c, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res