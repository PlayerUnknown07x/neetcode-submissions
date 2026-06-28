class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2)
                stack.append(num1)
                stack.append(num1+num2)
            elif ch == "C":
                stack.pop()
            elif ch == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(ch))
        print(stack)
        return sum(stack)

        