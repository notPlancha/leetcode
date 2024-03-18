import bisect

class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    invervals = [[-2, -1], [10**5 + 1, 10**5 + 2]]
    for point in points:
        invervals = self.insert(invervals, point)
    return len(intervals) - 2
  def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    if len(intervals) == 0:
      return [newInterval]
    ind1 = bisect.bisect(intervals, newInterval[0], key=lambda x: x[0])
    inside1 = newInterval[0] <= intervals[ind1 - 1][1]
    ind2 = bisect.bisect(intervals, newInterval[1], key=lambda x: x[1])
    inside2 = newInterval[1] >= intervals[ind2][0]
    if inside1 and inside2:
      # consume both of newInterval
      ret =  intervals[0:ind1-1] + [[intervals[ind1 - 1][0], intervals[ind2][1]]] + intervals[ind2 + 1:len(intervals)]
    elif not inside1 and inside2:
      # consume only end of newInterval
      ret =  intervals[0:ind1] + [[newInterval[0], intervals[ind2][1]]] + intervals[ind2 + 1:len(intervals)]
    elif inside1 and not inside2:
      # consume only start of newInterval
      ret =  intervals[0:ind1 - 1] + [[intervals[ind1-1][0], newInterval[1]]] + intervals[ind2 :len(intervals)]
    else:
      # consume neither
      ret =  intervals[0:ind1] + [newInterval] + intervals[ind2:len(intervals)]
    return ret[1:-1]