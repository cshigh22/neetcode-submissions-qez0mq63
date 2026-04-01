class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        global_max = nums[0]
        
        for i in range(1, len(nums)):
            current_min = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            current_max = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            global_max = max(global_max, current_max)

            prev_min = current_min
            prev_max = current_max

        return global_max