"""
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

1. Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
2. Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
3. The prefix and the suffix should not intersect at any index.
4. The characters from the prefix and suffix must be the same.
5. Delete both the prefix and the suffix.

Return the minimum length of s after performing the above operation any number of times (possibly zero times).
"""

import itertools as it

class Solution:
  def minimumLength(self, s: str) -> int:

    try:
      while True:
        if len(s) == 1: return 1
        letter1 = s[i := 0]
        letter2 = s[j := len(s) - 1]
        if letter1 != letter2:
          return len(s)
        while s[i + 1] == letter1:
          i += 1
        while s[j - 1] == letter1:
          j -= 1
        s = s[i+1: j]
    except IndexError:
      return 0


  def test(self):
    from icecream import ic
    assert ic(self.minimumLength("ca")) == 2
    assert ic(self.minimumLength("cabaabac")) == 0
    assert ic(self.minimumLength("aabccabba")) == 3
    assert ic(self.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb")) == 1
    assert ic(self.minimumLength("b")) == 1

if __name__ == "__main__":
  sol = Solution()
  sol.test()
  print("All tests passed!")
