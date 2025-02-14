class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        i = 0
        
        # append all non conflictin intervals from start in answer array
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i+=1
        
        # merge all conflicting intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)
        
        # append the remaining non-inflicting interval intervals in ans:
        while i <len(intervals):
            ans.append(intervals[i])
            i+=1
        return ans 

        