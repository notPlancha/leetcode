# Given an array of integers nums and an integer k, return the number of
# contiguous subarrays where the product of all the elements in the subarray is strictly
# less than k.
#
#
#  Example 1:
#
#
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
#
#
#  Example 2:
#
#
# Input: nums = [1,2,3], k = 0
# Output: 0
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 3 * 10⁴
#  1 <= nums[i] <= 1000
#  0 <= k <= 10⁶
#
#
#  Related Topics Array Sliding Window 👍 6438 👎 200

from icecream import ic

# leetcode submit region begin(Prohibit modification and deletion)
from math import prod
class Solution:
  def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
    if prod(nums) < k: return len(nums) * (len(nums) + 1) // 2
    left = 0
    right = -1
    curr = 1
    expanding = True
    ret = set()
    while True:
      if expanding:
        right += 1
        if right == len(nums): break
        nextt = curr * nums[right]
        if nextt >= k:
          expanding = False
          # right is excluding already
          ret.update((i, j) for i in range(left, right) for j in range(i, right)) # experiment with creating a set instead
        curr = nextt
      else:
        a, b = sorted((curr, nums[left]))
        nextt = b // a
        if nextt < k:
          expanding = True
        elif left == right:
          right += 1
          if right == len(nums): break
        curr = nextt
        left += 1
    # do a last time if valid
    if nextt < k:
      pass
      ret.update((i, j) for i in range(left, right) for j in range(i, right))
    return len(ret)

# leetcode submit region end(Prohibit modification and deletion)
ic(Solution().numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3], 19)) # 18
ic(Solution().numSubarrayProductLessThanK([1,2,3], 0)) # 0

ic(Solution().numSubarrayProductLessThanK([10,5,2,6], 100)) # 8
ic(Solution().numSubarrayProductLessThanK([1,1,1], 2)) # 6
ic(Solution().numSubarrayProductLessThanK([200,10,5,2,6], 100)) # 8
ic(Solution().numSubarrayProductLessThanK([1,2,3,4,5], 1)) # 0