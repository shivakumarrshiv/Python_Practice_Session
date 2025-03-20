class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


height = list(map(int, input("Enter heights separated by spaces: ").split()))
data=Solution()
print(data.maxArea(height))
