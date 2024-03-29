# You are given an integer array nums and a positive integer k.
#
#  Return the number of subarrays where the maximum element of nums appears at
# least k times in that subarray.
#
#  A subarray is a contiguous sequence of elements within an array.
#
#
#  Example 1:
#
#
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1
# ,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
#
#
#  Example 2:
#
#
# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁵
#  1 <= nums[i] <= 10⁶
#  1 <= k <= 10⁵
#
#
#  Related Topics Array Sliding Window 👍 988 👎 49


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def countSubarrays(self, nums: list[int], k: int) -> int:
    right = currCount = ret = 0
    left = last_max = -1
    m = max(nums)
    while right < len(nums):
      num = nums[right]
      if num == m: currCount += 1
      if currCount >= k:
        while True:
          left += 1
          num = nums[left]
          if num == m:
            currCount -= 1
            if currCount < k:
              if last_max == -1: # first time
                # first time will look foward and backwards
                # 13232231, k=2, len(8) ->
                #  323  3232  32322  323223  3232231,
                # 1323 13232 132322 1323223 13232231
                ret += (len(nums) - right) * (left + 1) # (8 - 3) (1 + 1) = 5 * 2
              else:
                # 13232231, k=2, len(8) ->
                #  3223,  32231,
                # 23223, 232231
                # 323223 ja e repetido
                ret += (len(nums) - right) * (left - last_max) # (8 - 6) (3 - 1) = 2 * 2
              last_max = left
              break
      right += 1
    return ret
# leetcode submit region end(Prohibit modification and deletion)

from icecream import ic

ic(Solution().countSubarrays([1,3,2,3,3], 2)) # 6
ic(Solution().countSubarrays([1,3,2,3,2,2,3, 1], 2)) # 14
ic(Solution().countSubarrays([1,3,2,3,3,2], 2)) # 10
ic(Solution().countSubarrays([1,1,3,2,3,3,2], 2)) # 13
ic(Solution().countSubarrays([1,4,2,1], 3)) # 0
ic(Solution().countSubarrays([61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82], 2)) # 224
ic(Solution().countSubarrays([21,11,13,15,16,21,8,9,6,21], 2)) # 10