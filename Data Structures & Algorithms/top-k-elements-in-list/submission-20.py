class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if (k == len(nums)):
            return nums
        count_map = {}
        for number in nums:
            count_map[number] = count_map.get(number,0)+1
        bucket_list = [[] for _ in range(len(nums)+1)]
        for num , frequency in count_map.items():
            bucket_list[frequency].append(num)
        results = []
        print(bucket_list)
        for index in range(len(bucket_list) -1 , 0 , -1):
            for num in bucket_list[index]:
                results.append(num)
                if len(results) == k:
                    return results
        return results
        
        
        

        