"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from functools import cmp_to_key
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 1 or len(intervals) == 0:
            return True
        def sortlogic(a : Interval , b : Interval) ->int:
            if a.start < b.start:
                return -1
            else:
                return 1
        intervals.sort(key = cmp_to_key(sortlogic))
        s = intervals[0].start
        e = intervals[0].end
        for i in range(1,len(intervals)):
            if s == intervals[i].start or s < intervals[i].start <e:
                return False
            s = intervals[i].start 
            e = intervals[i].end
        return True


