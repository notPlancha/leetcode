# Given an unsorted integer array nums. Return the smallest positive integer
# that is not present in nums.
#
#  You must implement an algorithm that runs in O(n) time and uses O(1)
# auxiliary space.
#
#
#  Example 1:
#
#
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#
#
#  Example 2:
#
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#
#
#  Example 3:
#
#
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁵
#  -2³¹ <= nums[i] <= 2³¹ - 1
#
#
#  Related Topics Array Hash Table 👍 15855 👎 1783
from icecream import ic

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def firstMissingPositive(self, nums: list[int]) -> int:
    nums = [num for num in nums if num > 0]
    for i in range(len(nums)):
      index = abs(nums[i]) - 1
      if index >= len(nums): continue
      nums[index] = -abs(nums[index])
    for i in range(len(nums)):
      if nums[i] > 0: return i + 1
    return len(nums) + 1
# leetcode submit region end(Prohibit modification and deletion)

ic(Solution().firstMissingPositive([1,2,0])) # 3
ic(Solution().firstMissingPositive([3,4,-1,1])) # 2
ic(Solution().firstMissingPositive([7,8,9,11,12])) # 1