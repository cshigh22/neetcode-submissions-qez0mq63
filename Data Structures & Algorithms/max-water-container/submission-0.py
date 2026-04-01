class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        score = 0

        while left < right:
            score = max(score, (right - left) * min(heights[left], heights[right]))

            if heights[left] > heights[right]:
                right -= 1
            else:
                    left += 1

        return score