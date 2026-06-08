class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)
        max_streak = 0
        for num in hash_map:
            if num-1 not in hash_map:
                current_num = num
                current_max = 1
                while(1):
                    if (current_num+1) not in hash_map:
                        break
                    current_max+=1
                    current_num = current_num+1
                max_streak = max(current_max,max_streak)
        return max_streak

        

        