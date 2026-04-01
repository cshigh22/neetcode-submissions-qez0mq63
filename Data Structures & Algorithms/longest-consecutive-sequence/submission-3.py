class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # sorted_nums = sorted(nums)
        # max_len, current = 1, 1
        # for i in range(1, len(sorted_nums)):
        #     if sorted_nums[i] == sorted_nums[i-1]:
        #         continue
        #     elif sorted_nums[i] == sorted_nums[i-1] + 1:
        #         current += 1
        #         max_len = max(max_len, current)
        #     else:
        #         current = 1
        # return max_len
        numSet = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in numSet:
                length = 0
                while (i + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest