# Given an integer array nums of length n where all the integers of nums are in
# the range [1, n] and each integer appears once or twice, return an array of all
# the integers that appears twice.
#
#  You must write an algorithm that runs in O(n) time and uses only constant
# extra space.
#
#
#  Example 1:
#  Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
#
#  Example 2:
#  Input: nums = [1,1,2]
# Output: [1]
#
#  Example 3:
#  Input: nums = [1]
# Output: []
#
#
#  Constraints:
#
#
#  n == nums.length
#  1 <= n <= 10⁵
#  1 <= nums[i] <= n
#  Each element in nums appears once or twice.
#
#

from icecream import ic

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def findDuplicates(self, nums: list[int]) -> list[int]:
    ret = []
    for num in nums:
      num = -abs(num)
      if nums[num] < 0:
        ret.append(-num)
      else:
        nums[num] = -abs(nums[num])
    return ret
# leetcode submit region end(Prohibit modification and deletion)

ic(Solution().findDuplicates([4,3,2,7,8,2,3,1])) # [2,3]
ic(Solution().findDuplicates([1,1,2])) # [1]
ic(Solution().findDuplicates([1])) # []

