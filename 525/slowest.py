from collections import Counter
from more_itertools import windowed

class Solution:
  def findMaxLength(self, nums: list[int]) -> int:
    if len(nums) % 2 == 0: sub = 0
    else: sub = 1
    for i in range(len(nums) - sub, 0, -2):
      for window in windowed(nums, i):
        c = Counter(window)
        if c[0] == c[1]: return i
    return 0