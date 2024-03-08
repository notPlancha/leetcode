from collections import Counter

class Solution:
  def maxFrequencyElements(self, nums: list[int]) -> int:
    c = Counter(nums)
    li = list(c.values())
    m = max(li)
    filtered = filter(lambda x: x == m, li)
    return len(list(filtered)) * m