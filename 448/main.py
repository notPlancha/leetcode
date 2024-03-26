# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.
#
#
#  Example 1:
#  Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
#
#  Example 2:
#  Input: nums = [1,1]
# Output: [2]
#
#
#  Constraints:
#
#
#  n == nums.length
#  1 <= n <= 10⁵
#  1 <= nums[i] <= n
#
#
#
#  Follow up: Could you do it without extra space and in O(n) runtime? You may
# assume the returned list does not count as extra space.
#
#  Related Topics Array Hash Table 👍 9269 👎 477

from icecream import ic

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    for num in nums:
      num = -abs(num)
      nums[num] = -abs(nums[num])
    return [i for i in range(1, 1 + len(nums)) if nums[-i] > 0]
# leetcode submit region end(Prohibit modification and deletion)

ic(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])) # [5,6]
ic(Solution().findDisappearedNumbers([1,1])) # [5,6]