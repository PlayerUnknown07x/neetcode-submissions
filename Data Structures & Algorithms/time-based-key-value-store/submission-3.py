class TimeMap:

    def __init__(self):
        self.keyTime = defaultdict(list)
        self.timeValue = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyTime[key].append(timestamp)
        self.timeValue[timestamp] = value
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyTime.keys():
            return ""
        if self.keyTime[key][0] > timestamp:
            return ""
        if self.keyTime[key][-1] <= timestamp:
            return self.timeValue[self.keyTime[key][-1]]
        left = 0
        right = len(self.keyTime[key]) - 1
        result = ""
        while(left <= right):
            mid = left + (right-left)//2
            if self.keyTime[key][mid] == timestamp:
                return self.timeValue[timestamp]
            elif self.keyTime[key][mid] < timestamp:
                result = self.keyTime[key][mid]
                left = mid + 1
            else:
                right = mid - 1 
        return self.timeValue[result]
        
