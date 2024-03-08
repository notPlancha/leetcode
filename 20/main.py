from collections import deque
class Solution:
  def isValid(self, s: str) -> bool:
    deepness = deque()
    for i in s:
      if i in ["(", "{", "["]:
        deepness.append(i)
      else:
        if len(deepness) == 0: return False
        removed = deepness.pop()
        if (i, removed) not in [(")", "("), ("}", "{"), ("]", "[")]:
          return False
    return len(deepness) == 0


  def test(self):
    from icecream import ic
    assert ic(self.isValid("()")) is True
    assert ic(self.isValid("()[]{}")) is True
    assert ic(self.isValid("(]")) is False
    assert ic(self.isValid("([])") is True)
    assert ic(self.isValid("([)]")) is False


if __name__ == "__main__":
  sol = Solution()
  sol.test()
  print("All tests passed!")