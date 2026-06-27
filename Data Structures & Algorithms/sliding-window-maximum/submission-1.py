class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result =[]
        n = len(nums)
        i = 0
        
        for i in range(n-k+1):
            j = i+k
            maxi = max(nums[i:j])
            result.append(maxi)
        return result
        
        