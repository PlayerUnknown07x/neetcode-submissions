class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack = []
        for ch in s:
            if ch in d.keys():
                stack.append(d[ch])
            else:
                if stack and ch != stack[-1]:
                    return False
                elif not stack:
                    return False
                stack.pop()
        return len(stack) == 0
