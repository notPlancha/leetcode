# We have n cities labeled from 1 to n. Two different cities with labels x and
# y are directly connected by a bidirectional road if and only if x and y share a
# common divisor strictly greater than some threshold. More formally, cities with
# labels x and y have a road between them if there exists an integer z such that
# all of the following are true:
#
#
#  x % z == 0,
#  y % z == 0, and
#  z > threshold.
#
#
#  Given the two integers, n and threshold, and an array of queries, you must
# determine for each queries[i] = [ai, bi] if cities ai and bi are connected
# directly or indirectly. (i.e. there is some path between them).
#
#  Return an array answer, where answer.length == queries.length and answer[i]
# is true if for the iᵗʰ query, there is a path between ai and bi, or answer[i] is
# false if there is no path.
#
#
#  Example 1:
#
#
# Input: n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
# Output: [false,false,true]
# Explanation: The divisors for each number:
# 1:   1
# 2:   1, 2
# 3:   1, 3
# 4:   1, 2, 4
# 5:   1, 5
# 6:   1, 2, 3, 6
# Using the underlined divisors above the threshold, only cities 3 and 6 share
# a common divisor, so they are the
# only ones directly connected. The result of each query:
# [1,4]   1 is not connected to 4
# [2,5]   2 is not connected to 5
# [3,6]   3 is connected to 6 through path 3--6
#
#
#  Example 2:
#
#
# Input: n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
# Output: [true,true,true,true,true]
# Explanation: The divisors for each number are the same as the previous
# example. However, since the threshold is 0,
# all divisors can be used. Since all numbers share 1 as a divisor, all cities
# are connected.
#
#
#  Example 3:
#
#
# Input: n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
# Output: [false,false,false,false,false]
# Explanation: Only cities 2 and 4 share a common divisor 2 which is strictly
# greater than the threshold 1, so they are the only ones directly connected.
# Please notice that there can be multiple queries for the same pair of nodes [
# x, y], and that the query [x, y] is equivalent to the query [y, x].
#
#
#
#  Constraints:
#
#
#  2 <= n <= 10⁴
#  0 <= threshold <= n
#  1 <= queries.length <= 10⁵
#  queries[i].length == 2
#  1 <= ai, bi <= cities
#  ai != bi
#
#
#  Related Topics Array Math Union Find Number Theory 👍 575 👎 33

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def areConnected(self, n: int, threshold: int, queries: list[tuple[int, int]]) -> list[bool]:
    if threshold == 0: return [True] * len(queries)
    smaller_numbers_to_not_pool = list(range(1, threshold)) # treshold is strict
    pools = {}
    current_pool = 0
    for before in smaller_numbers_to_not_pool: # pools that are alone
      pools[before] = current_pool
      current_pool += 1
    for vertical in range(threshold, n//2 + 1):
      if vertical in pools:
        continue # already visited, skip
      horizontal = 0 # vertical goes up by 1, horizontal goes up by itself
      horizontal_i = 0
      current_pool += 1
      while horizontal < n: # new pool line
        checkBiggers = True # 7*7
        horizontal_i += 1
        horizontal += vertical
        if (horizontal_i - 1) % vertical == 0: # already is making this pool so we can skip
          pools[horizontal] = current_pool
          continue
        if horizontal_i > vertical: # start doing inner pools
          #region add small ones first
          for i in smaller_numbers_to_not_pool:
            pools[horizontal_i * i] = current_pool
          #endregion
          if checkBiggers:
            inner_vertical = horizontal_i * horizontal_i # (3*7, 4*7 ... already seen)
            if inner_vertical > threshold:
              checkBiggers = False # if it's bigger pool is for number bigger than n
            while inner_vertical < threshold: # single inner pool
              pools[inner_vertical] = current_pool
              inner_vertical += horizontal_i
        else:
          pools[horizontal] = current_pool
    # the rest
    for rest in range(n//2 + 1, n + 1):
      if rest not in pools:
        current_pool += 1
        pools[rest] = current_pool
    return [pools[a] == pools[b] for a, b in queries]



# leetcode submit region end(Prohibit modification and deletion)

from icecream import ic
# ic(Solution().subarraysWithKDistinct([1,2,1,2,3], k = 2)) # 7
# ic(Solution().subarraysWithKDistinct([1,2,1,3,4], k = 3)) # 3
# ic(Solution().subarraysWithKDistinct([1,2,1,3,4,4], k = 3)) # 4
# ic(Solution().subarraysWithKDistinct([1,2], k = 1)) # 2
# ic(Solution().subarraysWithKDistinct([2,1,2,1,2], k = 2)) # 10
if __name__ == '__main__':
  tests = [
    ic(Solution().areConnected(n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]])) == [False,False,True],
    ic(Solution().areConnected(n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]])) == [True,True,True,True,True],
    ic(Solution().areConnected(n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]])) == [False,False,False,False,False],
    ic(Solution().areConnected(n = 9, threshold = 1, queries = [[6,8],[6,9],[8,9]])) == [True,True,True]
  ]
  for i,t in enumerate(tests):
    print(f"Test-{i+1} {'PASSED' if t else 'FAILED'}")
  print(f"Failed {len(tests)-sum(tests)} of {len(tests)} tests")
# from math import gcd
# class Solution:
#   def areConnected(self, n: int, threshold: int, queries: list[tuple[int, int]]) -> list[bool]:
#     ret = [False] * len(queries)
#     for i in range(len(queries)):
#       a = queries[i][0]
#       b = queries[i][0]
#       if a < threshold or b < threshold:
#         continue # will always be alone
#       result = gcd(a,b)
#       if result == 1:
#         continue
#       elif gcd(a, b) > threshold:
#         ret[i] = True
#         continue
#
#       else:
#     return ret
