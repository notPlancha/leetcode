"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

from collections import defaultdict, Counter
from line_profiler import profile


class Solution:
  @profile
  def minWindow(self, s: str, t: str) -> str:
    letters_of_t = Counter(t)
    t_len = len(t)  # at least
    ret: str | None = None

    for pointer_s, value_s in enumerate(s):  # or s[:-len(t) + 1] (until it's possible) but will raise smts
      if value_s in letters_of_t:
        letters_of_t_copy: Counter = letters_of_t.copy()  # so it doens't remove the first one
        letters_of_t_copy -= Counter(s[pointer_s: pointer_s + t_len])  # execute on current without checking (opt)
        # letters_of_t_copy = +letters_of_t_copy # output already rejects zero or less (.subtract doesn't)
        if letters_of_t_copy.total() == 0: return s[pointer_s: pointer_s + t_len]  # smallest possible
        enumStart = pointer_s + t_len
        # count from the current pointer
        for inner_pointer_s, inner_value_s in enumerate(s[enumStart:], start=enumStart):
          if letters_of_t_copy[inner_value_s] != 0:
            letters_of_t_copy[inner_value_s] -= 1
            if letters_of_t_copy.total() == 0:
              # found match
              if ret is None:
                ret = s[pointer_s: inner_pointer_s + 1]  # batota
              else:
                ret = min(ret, s[pointer_s: inner_pointer_s + 1], key=len)  # n sei pq ele se queixa
              break
    if ret is None:
      return ""
    else:
      return ret

  def test(self):
    from icecream import ic
    assert ic(self.minWindow("ADOBECODEBANC", "ABC")) == "BANC"
    assert ic(self.minWindow("a", "a")) == "a"
    assert ic(self.minWindow("a", "aa")) == ""


if __name__ == "__main__":
  sol = Solution()
  sol.test()
  print("All tests passed!")
