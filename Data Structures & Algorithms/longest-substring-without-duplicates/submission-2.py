class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        max_length = 1
        n = len(s)
        hash_map = set()
        j = i
        while(j<n):
            while(s[j] in hash_map):
                max_length = max(max_length , j-i)
                hash_map.remove(s[i])
                i+=1
            hash_map.add(s[j])
            j += 1
        max_length = max(max_length,j-i)
        return max_length
        