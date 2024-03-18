# You are given an array of non-overlapping intervals intervals where intervals[
# i] = [starti, endi] represent the start and the end of the iᵗʰ interval and
# intervals is sorted in ascending order by starti. You are also given an interval
# newInterval = [start, end] that represents the start and end of another interval.
#
#  Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
#  Return intervals after the insertion.
#
#  Note that you don't need to modify intervals in-place. You can make a new
# array and return it.
#
#
#  Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
#  Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
#
#  Constraints:
#
#
#  0 <= intervals.length <= 10⁴
#  intervals[i].length == 2
#  0 <= starti <= endi <= 10⁵
#  intervals is sorted by starti in ascending order.
#  newInterval.length == 2
#  0 <= start <= end <= 10⁵
#
#
#  Related Topics Array 👍 9575 👎 727
from icecream import ic
# leetcode submit region begin(Prohibit modification and deletion)
import bisect
# fazer de forma diferente (linear)
class Solution:
  def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    if len(intervals) == 0: return [newInterval]
    ind1 = bisect.bisect(intervals, newInterval[0], key=lambda x: x[0]) - 1
    inside1 = intervals[ind1][0] <= newInterval[0] <= intervals[ind1][1]
    ind2 = bisect.bisect(intervals, newInterval[1], key=lambda x: x[1])
    if ind2 == len(intervals):
      if ind1 == -1: return [newInterval]
      if inside1: return intervals[0:ind1] + [[intervals[ind1][0], newInterval[1]]]
      else: return intervals + [newInterval]
    else:
      inside2 = intervals[ind2][0] <= newInterval[1] <= intervals[ind2][1]
    if inside1 and inside2:
      # consume both
      return intervals[0:ind1] + [[intervals[ind1][0], intervals[ind2][1]]] + intervals[ind2 + 1:len(intervals)]
    elif not inside1 and inside2:
      # consume only right
      return intervals[0:ind1 - 1] + [[newInterval[0], intervals[ind2][1]]] + intervals[ind2 + 1:len(intervals)]
    elif inside1 and not inside2:
      # consume only left
      return intervals[0:ind1] + [[intervals[ind1][0], newInterval[1]]] + intervals[ind2 :len(intervals)]
    else:
      # consume none
      if ind1 + 1 == ind2: return intervals[0:ind1 + 1] + [newInterval] + intervals[ind2:len(intervals)]
      return intervals[0:ind1-1] + [newInterval] + intervals[ind2:len(intervals)]
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
  s = Solution()
  assert ic(s.insert([[1,3],[6,9]], [2,5])) == [[1,5],[6,9]]
  assert ic(s.insert([[1,3],[6,9]], [4,5])) == [[1, 3], [4, 5], [6, 9]]
  assert ic(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))== [[1,2],[3,10],[12,16]]
  assert ic(s.insert([[1,5]], [2,7])) == [[1,7]]
  assert ic(s.insert([[1,3], [4,5]], [6,7])) == [[1,3], [4,5], [6,7]]
  assert ic(s.insert([[3,4], [5,6]], [1,2]))== [[1,2], [3,4], [5,6]]
  assert ic(s.insert([[1,4], [5,6]], [1,2]))== [[1,4], [5,6]]
  assert ic(s.insert([], [1,2]))== [[1,2]]
  assert ic(s.insert([[2,5],[6,7],[8,9]],[0,10]))== [[0,10]]
  print("Tests passed")
