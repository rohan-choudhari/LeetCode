"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        i = 0
        while i<=(len(intervals)-2):
            j = i+1
            while j<=(len(intervals)-1):
                if (intervals[i].end >= intervals[j].start):
                    intervals[i].end = max(intervals[j].end, intervals[i].end)
                    intervals.pop(j)
                else:
                    j+=1
            i+=1

    def printIntervals(self, intervals):
        for i in intervals:
            print(i.start,"\t",i.end)

    def printInterval(self, interval):
        print(interval.start,"\t",interval.end)

leetCode = Solution()
intervals = []

if 0:
    intervals.append(Interval(1,4))
    intervals.append(Interval(3,7))
    intervals.append(Interval(5,6))
    intervals.append(Interval(8,12))
    intervals.append(Interval(14,17))
elif 0:
    intervals.append(Interval(1,3))
    intervals.append(Interval(2,6))
    intervals.append(Interval(8,10))
    intervals.append(Interval(15,18))
elif 1:
    intervals.append(Interval(1,4))
    intervals.append(Interval(4,5))

print("Before merging:")
leetCode.printIntervals(intervals)
leetCode.merge(intervals)
print("\nAfter merging:")
leetCode.printIntervals(intervals)


