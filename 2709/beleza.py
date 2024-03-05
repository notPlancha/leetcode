import math
from collections import Counter

class Solution:
  def canTraverseAllPairs(self, nums: list[int]) -> bool:
    if len(nums) == 1: return True
    nums = Counter(nums)
    if 1 in nums: return False

    nums = sorted(nums.keys(), reverse=True)

    for i in range(len(nums) - 1):
      for j in range(i + 1, len(nums)):
        if math.gcd(nums[i], nums[j]) > 1:
          nums[j] *= nums[i]
          break
      else:
        return False
    return True
