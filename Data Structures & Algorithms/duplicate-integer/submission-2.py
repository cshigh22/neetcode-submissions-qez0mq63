class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # box = []

        # for i in nums:
        #     if i not in box:
        #         box.append(i)
        # return len(box) != len(nums)

        # more efficient way:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False