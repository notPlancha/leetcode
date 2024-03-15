# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
#
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#  You must write an algorithm that runs in O(n) time and without using the
# division operation.
#
#
#  Example 1:
#  Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
#  Example 2:
#  Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
#  Constraints:
#
#
#  2 <= nums.length <= 10⁵
#  -30 <= nums[i] <= 30
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#
#  Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
#
#  Related Topics Array Prefix Sum 👍 21802 👎 1326
from icecream import ic
import sympy as sp
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    answer = [1 for _ in nums]
    for i in range(1, len(nums)):
      answer[i] = nums[i-1] * answer[i-1]
    ajuda = nums[-1]
    for i in range(len(nums)-2, 0, -1):
      answer[i] = answer[i] * ajuda
      ajuda *= nums[i]
    answer[0] = ajuda
    return answer
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
  a, b, c, d, e, f = sp.symbols('a b c d e f')
  Solution().productExceptSelf([a, b, c, d, e, f])
  assert ic(Solution().productExceptSelf([6,6,6,6,6,6])) == ic([6**5 for _ in range(6)])
  assert ic(Solution().productExceptSelf([1,2,3,4,5,6])) == [720,360,240,180,144,120]
  assert ic(Solution().productExceptSelf([1,2,3,4])) == [24,12,8,6]
  assert ic(Solution().productExceptSelf([-1,1,0,-3,3])) == [0,0,9,0,0]
