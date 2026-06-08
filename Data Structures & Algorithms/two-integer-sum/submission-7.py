class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rest = {}
        for i in range (len(nums)):
                rest[nums[i]] = i
        print(rest)
        for i in range (len(nums)):
            wanted = target - nums[i]
            if(wanted in rest and rest[wanted] != i):
                return [i,rest[wanted]]
        return []
        