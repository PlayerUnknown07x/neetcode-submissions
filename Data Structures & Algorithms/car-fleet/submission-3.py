class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [-1 for _ in range(target+1)]
        fleet = 0
        fleet_time = float('-inf')
        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            times[position[i]] = time
        for i in range(len(times)-1,-1,-1):
            if times[i] != -1:
                if times[i] > fleet_time:
                    fleet += 1
                    fleet_time = times[i]
        return fleet








            
        