class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        digits[-1] = 0
        carry = 1
        for j in range(len(digits)-2,-1,-1):
            initial = digits[j]+1
            final = initial%10
            digits[j] = final
            carry = initial//10
            if carry == 0:
                return digits
        return [1]+digits

        