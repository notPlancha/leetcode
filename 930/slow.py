from more_itertools import substrings
class Solution:
  def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
    ret = 0
    for comb in substrings(nums):
      if comb.count(1) == goal:
        ret += 1
    return ret