class MinStack:

    def __init__(self):
        self.Stack = []
    def push(self, val: int) -> None:
        self.Stack.append(val)
    def pop(self) -> None:
        self.Stack.pop()
    def top(self) -> int:
        return self.Stack[len(self.Stack)-1]
    def getMin(self) -> int:
        return min(self.Stack)
        
