class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = Counter(s1)
        n = len(s2)
        m = len(s1)
        i = 0
        j = 0
        while i <= n-m and j < n:
            print(i)
            if s2[i] not in s1:
                i +=1
                continue
            j = i+m
            if Counter(s2[i:j]) == c1:
                return True
            i += 1
        return False
            
            
        