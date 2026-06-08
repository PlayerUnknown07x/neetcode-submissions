class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordList = {}
        for word in strs:
            Wc = [0]*26
            for ch in word:
                index = ord(ch) - ord('a')
                Wc[index]+=1
            key = tuple(Wc)
            if(word == "hat"):
                    print(key)
            if(key in wordList):
                wordList[key].append(word)
            else:
                wordList[key] = [word]
        return list(wordList.values())


