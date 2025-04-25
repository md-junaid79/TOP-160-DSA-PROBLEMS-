
class Solution:
    
    def minRemoval(self,intervals):
        cnt = 0
    
        # Sort by minimum starting point
        intervals.sort()
    
        end = intervals[0][1]
        for i in range(1, len(intervals)):
    
            # If the current starting point is less than
            # the previous interval's ending point
            # (ie. there is an overlap)
            if intervals[i][0] < end:
              
                # Increase cnt and remove the interval
                # with the higher ending point
                cnt += 1
                end = min(intervals[i][1], end)
    
            # Incase of no overlapping, this interval is 
            # not removed and 'end' will be updated
            else:
                end = intervals[i][1]
    
        return cnt
    
        
