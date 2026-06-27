class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] >0:
            return []
        n = len(nums)
        result = []
        i = 0
        while i < (n-2):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i+1
            k = n-1
            while(j < k):
                if nums[i]+nums[j]+nums[k] == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    while(j < k and nums[j+1] == nums[j]):
                        j +=1
                    j += 1
                    while(j < k and nums[k-1] == nums[k]):
                        k -= 1
                    k -= 1
                elif nums[i]+nums[j]+nums[k] > 0:
                    while(j < k and nums[k-1] == nums[k]):
                        k -= 1
                    k -= 1
                else :
                    while(j < k and nums[j+1] == nums[j]):
                        j +=1
                    j += 1
            i += 1
        return result
        
        