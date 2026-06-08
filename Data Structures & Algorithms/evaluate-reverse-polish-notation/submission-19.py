class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        nums = []
        for ch in tokens:
            if(ch not in operators):
                nums.append(int(ch))
            else:
                print(nums)
                num1 = nums.pop()
                num2 = nums.pop()
                match ch:
                    case "+":
                        nums.append(num2+num1)
                    case "-":
                        nums.append(num2-num1)
                    case "*":
                        nums.append(num1*num2)
                    case "/":
                        print("num2 ",num2," num1 ",num1)
                        nums.append(int(num2/num1))
        print(nums)
        return nums[-1]
            



        