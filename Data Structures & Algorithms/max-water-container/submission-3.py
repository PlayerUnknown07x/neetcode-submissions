class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_volume = 0
        while(j>i):
            current_volume = min(heights[i],heights[j])*(j-i)
            max_volume = max(max_volume,current_volume)
            if(heights[i]<heights[j]):
                i += 1
            else:
                j -= 1
        return max_volume
        