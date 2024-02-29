from icecream import ic
from pytictoc import TicToc
import math
from collections import defaultdict


# Copyright (c) 2018 Indrajit Jana - https://mit-license.org/
def factor(num: int) -> int:
  if num == 1:
    return 2
  if num == 2 or num % 2 == 0:
    return 2
  if num == 3 or num % 3 == 0:  # dakra added
    return 3  # dakra added
  else:
    for i in range(6, int(math.sqrt(num)) + 7, 6):  # dakra Primes > 3 are all either
      if num % (i - 1) == 0: return i - 1  # dakra 5 mod 6 or
      if num % (i + 1) == 0: return i + 1  # dakra 1 mod 6
      # dakra saving all the tests for number which are 3 mod 6.
    else:
      return num
# Copyright (c) 2018 Indrajit Jana - https://mit-license.org/
def factors(num: int) -> list:
  fact = factor(num)
  new_num = num // fact
  factors = [fact]
  while new_num != 1:
    fact = factor(new_num)
    factors.append(fact)
    new_num //= fact
  return factors


class Solution:
  def canTraverseAllPairs(self, nums: list[int]) -> bool:
    if len(nums) == 1:
      return True
    if 1 in (nums := set(nums)):
      return False
    nums = list(nums)
    map = dict()


    # create factors
    for num in nums:
      map[num] = set(factors(num))
    # create graph
    graph = defaultdict(list)
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if len(map[nums[i]].intersection(map[nums[j]])) > 0:
          graph[i].append(j)
          graph[j].append(i)

    # dfs
    visited = set()
    stack = [0]
    while stack:
      node = stack.pop()
      if node not in visited:
        visited.add(node)
        stack.extend([n for n in graph[node] if n not in visited])
    return len(visited) == len(nums)

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
