from more_itertools import windowed
from collections import Counter
class Solution:
  def findMaxLength(self, nums: list[int]) -> int:

    # first
    if len(nums) % 2 == 0:
      sub = 0
      starts_s = sum(nums)
      if starts_s*2 == len(nums): return len(nums)
    else:
      starts_s = curr_s = sum(nums) - nums[-1]
      sub = 1
      if curr_s*2 == len(nums) - 1: return len(nums) - 1
      curr_s = curr_s - nums[0] + nums[1]
      if curr_s*2 == len(nums) - 1: return len(nums) - 1
    #firstend
    for window_size in range(len(nums) - sub - 2, 0, -2):
      starts_s = curr_s = starts_s - nums[window_size] - nums[window_size + 1]
      windows_iter = self.windows_index(nums, window_size)
      first = next(windows_iter)
      if curr_s*2 == window_size: return window_size
      for nextes in windows_iter:
        curr_s = curr_s - nums[nextes[0]-1] + nums[nextes[1]-1]
        if curr_s*2 == window_size: return window_size
    return 0

  def windows_index(self, nums, window_size):
    for i in range(len(nums) - window_size + 1):
      yield i, i+window_size