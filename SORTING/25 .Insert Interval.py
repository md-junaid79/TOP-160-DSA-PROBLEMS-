
class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        res = []
        i = 0
        n = len(intervals)
    
        # Add all intervals that come before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
    
        # Merge all overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        res.append(newInterval)
    
        # Add all the remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1
    
        return res
