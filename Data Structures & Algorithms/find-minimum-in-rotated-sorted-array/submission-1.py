class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        # Loop until the low and high pointers meet
        while low < high:
            mid = (low + high) // 2

            # Case 1: The pivot is on the right side of mid
            if nums[mid] > nums[high]:
                low = mid + 1
            # Case 2: The pivot is on the left side, or at mid itself
            else:
                high = mid
        
        # When the loop finishes, low and high will be at the index of the minimum element
        return nums[low]