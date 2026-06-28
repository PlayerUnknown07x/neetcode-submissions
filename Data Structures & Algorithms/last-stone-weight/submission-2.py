class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            r1 = stones.pop()
            r2 = stones.pop()
            if r1 == r2:
                continue
            stones.append(max(r1,r2)-min(r1,r2))
            stones.sort()
        if stones:
            return stones[0]
        return 0
        