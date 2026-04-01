class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # nums.sort()

        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i-1]:
        #         continue
        #     l, r = i + 1, len(nums) - 1
        #     while l < r:
        #         threeSum = a + nums[l] + nums[r]
        #         if threeSum > 0:
        #             r -= 1
        #         elif threeSum < 0:
        #             l += 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             l += 1
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1
        # return res
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate values for i

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # we need a bigger sum
                else:
                    right -= 1  # we need a smaller sum

        return res
