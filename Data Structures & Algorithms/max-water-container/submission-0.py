class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_height = max(max_height, current_height)
        # max_amount = 

        max_height = 0
        max_amount = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            max_height = min(heights[left], heights[right])
            max_amount = max(max_amount, (max_height * (right - left)))
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_amount