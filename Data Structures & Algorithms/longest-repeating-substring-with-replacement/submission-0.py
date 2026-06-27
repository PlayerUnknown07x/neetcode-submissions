class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = i
        dicti = {}
        max_freq = 1
        max_length =0
        n = len(s)
        while(j<n):
            dicti[s[j]] = dicti.get(s[j], 0) + 1
            max_freq = max(max_freq,dicti[s[j]])
            if(j-i+1) > max_freq+k:
                dicti[s[i]] -= 1
                i += 1
            max_length = max(max_length,j-i+1)
            j += 1
        return max_length
            



        