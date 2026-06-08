class Solution:
    def trap(self, height: List[int]) -> int:
        last_height = height[0]
        volume = 0
        maxH = 0
        left_max = [0]*len(height)
        right_max = [0]*len(height)
        for i in range(len(height)):
            print("i :",i," maxH :",maxH)
            left_max[i] = maxH
            maxH = max(maxH , height[i])
        maxH = 0
        for i in range(len(height)-1 , -1 , -1):
            right_max[i] = maxH
            maxH = max(maxH,height[i])
        for i in range(len(height)):
            if(min(left_max[i],right_max[i])-height[i] < 0 ):
                continue
            volume += min(left_max[i],right_max[i])-height[i]
        return volume
