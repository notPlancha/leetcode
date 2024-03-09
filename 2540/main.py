class Solution:
  def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
    gen1 = iter(nums1)
    gen2 = iter(nums2)
    curr1 = next(gen1)
    curr2 = next(gen2)
    while True:
      if curr1 == curr2: return curr1
      elif curr1 < curr2:
        curr1 = next(gen1, None)
        if curr1 is None: return -1
      else:
        curr2 = next(gen2, None)
        if curr2 is None: return -1