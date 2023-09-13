class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        best = min(height[l], height[r]) * (r - l)
        while (l < r):
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            if min(height[l], height[r]) * (r - l) > best:
                best = min(height[l], height[r]) * (r - l)
        return best