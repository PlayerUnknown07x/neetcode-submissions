class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while(j>i):
            if(numbers[i]+numbers[j]) > target:
                j -= 1
                print("numbers[i]+numbers[j] greater",numbers[i]+numbers[j])
            elif(numbers[i]+numbers[j]) < target:
                print("numbers[i]+numbers[j] lesser",numbers[i]+numbers[j])
                i += 1
            else:
                break
        return [i+1,j+1]

        