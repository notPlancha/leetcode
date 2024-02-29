from icecream import ic
from math import gcd
from array import array

class AdjanencyMatrix:
  def __init__(self, nums: list[int]):
    self.matrix = [array('b', [0 for _ in range(len(nums))]) for _ in range(len(nums))]
    for i in range(len(nums)):
      for j in range(i, len(nums)):
        # j > i sempre
        if gcd(nums[i], nums[j]) > 1:
          self.matrix[i][j] = 1
          self.matrix[j][i] = 1

  # check if it's disconected
  def dfs(self, vertex_i: int, visited: list[bool]) -> None:  # return is visited, and can be validated with all(visited)
    visited[vertex_i] = True
    for i in range(len(self.matrix[vertex_i])):
      if self.matrix[vertex_i][i] == 1 and not visited[i]:
        self.dfs(i, visited)


class Solution:
  def canTraverseAllPairs(self, nums: list[int]) -> bool:
    if len(nums) == 1:
      return True
    if 1 in (nums := set(nums)):
      return False
    nums = list(nums)
    ret = AdjanencyMatrix(nums)
    visited = [False for _ in range(len(nums))]
    ret.dfs(0, visited)
    return all(visited)

  def test(self):
    assert ic(self.canTraverseAllPairs(ic([2, 3, 6]))) is True
    assert ic(self.canTraverseAllPairs(ic([3, 9, 5]))) is False
    assert ic(self.canTraverseAllPairs(ic([4, 3, 12, 8]))) is True
    assert ic(self.canTraverseAllPairs(ic([3, 25]))) is False
    assert ic(self.canTraverseAllPairs(ic([30, 25]))) is True
    assert ic(self.canTraverseAllPairs(ic([1, 1]))) is False
    assert ic(self.canTraverseAllPairs(ic([1]))) is True
    assert ic(self.canTraverseAllPairs(ic([30]))) is True
    assert ic(self.canTraverseAllPairs(ic([30, 30]))) is True
    assert ic(self.canTraverseAllPairs(ic([63, 85, 70, 13, 30, 60, 65, 60, 75, 77, 70, 60]))) is True
    assert ic(self.canTraverseAllPairs(ic([45, 49, 20, 13, 21, 42, 30, 30, 39, 21, 28, 45, 22]))) is True


if __name__ == "__main__":
  sol = Solution()
  sol.test()
  print("All tests passed!")
