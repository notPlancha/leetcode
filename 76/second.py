"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""


class Solution:
  def minWindow(self, s: str, t: str) -> str:
    pass
  def test(self):
      from icecream import ic
      assert ic(self.minWindow("ADOBECODEBANC", "ABC")) == "BANC"
      assert ic(self.minWindow("a", "a")) == "a"
      assert ic(self.minWindow("a", "aa")) == ""
if __name__ == "__main__":
  s = Solution()
  s.test()
  print("All tests passed!")