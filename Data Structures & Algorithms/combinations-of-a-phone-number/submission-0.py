class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_pad = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [ch for ch in key_pad[int(digits)]]
        n = int(digits)%10
        
        return [x + y for x in self.letterCombinations(str(int(digits)//10)) for y in self.letterCombinations(str(n))]
        
        