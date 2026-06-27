class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left  = 0
        right = len(nums)-1
        while(left <= right):
            mid = left + (right-left)//2
            if mid != 0 and mid != len(nums)-1:
                if nums[mid] <= nums[mid-1] and nums[mid] <= nums[mid+1]:
                    return nums[mid]
            if nums[mid] >= nums[left]:
                if nums[right] >= nums[mid]:
                    return nums[left]
                left = mid + 1
            else:
                if nums[right] <= nums[mid]:
                    return nums[right]
                right  = mid -1
        return nums[0]