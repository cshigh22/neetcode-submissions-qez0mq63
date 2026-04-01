class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)
        furthest_reach = 0

        for i in range(len(nums)):
            if i > furthest_reach:
                return False
            
            furthest_reach = max(i + nums[i], furthest_reach)
        return True