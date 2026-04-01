class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        res = 0
        while left < right:
            count = (right- left) * min(heights[right], heights[left])
            res = max(res, count)

            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return res