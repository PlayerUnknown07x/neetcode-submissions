class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area,heights[i])
            j = i+1
            min_height = heights[i]
            while(j < len(heights)):
                min_height = min(min_height,heights[j])
                max_area = max(max_area,min_height*(j-i+1))
                j+=1
            if i == 2 :
                print(max_area)
        return max_area
            
            
        