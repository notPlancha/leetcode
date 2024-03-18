# There are some spherical balloons taped onto a flat wall that represents the
# XY-plane. The balloons are represented as a 2D integer array points where points[
# i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches
# between xstart and xend. You do not know the exact y-coordinates of the balloons.
#
#  Arrows can be shot up directly vertically (in the positive y-direction) from
# different points along the x-axis. A balloon with xstart and xend is burst by
# an arrow shot at x if xstart <= x <= xend. There is no limit to the number of
# arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any
# balloons in its path.
#
#  Given the array points, return the minimum number of arrows that must be
# shot to burst all balloons.
#
#
#  Example 1:
#
#
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
#
#
#  Example 2:
#
#
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4
# arrows.
#
#
#  Example 3:
#
#
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
#
#
#
#  Constraints:
#
#
#  1 <= points.length <= 10⁵
#  points[i].length == 2
#  -2³¹ <= xstart < xend <= 2³¹ - 1
#
#
#  Related Topics Array Greedy Sorting 👍 7257 👎 221

from icecream import ic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def findMinArrowShots(self, points: list[list[int]]) -> int:
    points.sort()
    ret = 0
    i_points = iter(points)
    curr = next(i_points)
    try:
      while True:
        ret += 1
        # find next point where end > start
        while True:
          if curr[1] < (g := next(i_points))[0]:
            curr = g
            break
          else:
            curr = self.merge(curr, g)
    except StopIteration:
      pass
    return ret
  def merge(self, i1: tuple[int, int], i2: tuple[int, int]):
    return max(i1[0], i2[0]), min(i1[1], i2[1])
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
  s = Solution()
  assert ic(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])) == 2
  assert ic(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])) == 4
  assert ic(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])) == 2
  assert ic(s.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]])) == 2
  assert ic(s.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])) == 2