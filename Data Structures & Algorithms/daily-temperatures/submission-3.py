class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0 for _ in range(n)]
        max_temp = float('-inf')
        max_temp_index = 0
        stack = []
        for i in range(n):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                result[a] = i-a
            stack.append(i)
        return result




        