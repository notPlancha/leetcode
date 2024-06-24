# Given an integer array nums and an integer k, return the number of good
# subarrays of nums.
#
#  A good array is an array where the number of different integers in that
# array is exactly k.
#
#
#  For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
#
#
#  A subarray is a contiguous part of an array.
#
#
#  Example 1:
#
#
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1],
#  [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
#
#
#  Example 2:
#
#
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2
# ,1,3], [1,3,4].
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 2 * 10⁴
#  1 <= nums[i], k <= nums.length
#
#
#  Related Topics Array Hash Table Sliding Window Counting 👍 5754 👎 91


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:
  def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
    right = currCount = ret = 0
    c = defaultdict(lambda: 0)
    left = -1
    lminus1 = len(nums) - 1
    while right <= lminus1:
      num = nums[right]
      right += 1
      c[num] += 1
      if c[num] == 1:
        # new number in subarray
        currCount += 1
        if currCount < k: continue
        pr = right + 1
        pl = left + 1
        # move right until another new number (or wall TODO)
        try:
          while c[nums[pr]] != 0:
            c[nums[pr]] += 1
            pr += 1
        except IndexError: pass
        # move left until we remove enough
        while c[nums[pl]] > 1:
          c[nums[pl]] -= 1
          pl -= 1
        ret += (pl - (left if left != -1 else 0)) * (pl - right)
        left = right
        right = pr
    return ret
# leetcode submit region end(Prohibit modification and deletion)
from icecream import ic
ic(Solution().subarraysWithKDistinct([1,2,1,2,3], k = 2)) # 7
ic(Solution().subarraysWithKDistinct([1,2,1,3,4], k = 3)) # 3
ic(Solution().subarraysWithKDistinct([1,2,1,3,4,4], k = 3)) # 4
ic(Solution().subarraysWithKDistinct([1,2], k = 1)) # 2
ic(Solution().subarraysWithKDistinct([2,1,2,1,2], k = 2)) # 10