class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        count_1 = {}
        count_2 = {}
        for i in range(len(s)):
            if s[i] in count_1:
                count_1[s[i]]+=1
            else:
                count_1[s[i]] = 1

            if(t[i] in count_2):
                count_2[t[i]] += 1
            else:
                count_2[t[i]] = 1
        return count_1 == count_2
                
            
        

        