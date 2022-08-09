class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        area = 0
        while left <= right:
            temp = min(height[left],height[right])*(right-left)
            area = max(area, temp)
            #使移动后的容器的高尽量大:移动　值小的一边
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area