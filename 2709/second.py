"""
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can
traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest
common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of
traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.
"""

from icecream import ic

from math import gcd
from collections import deque

from line_profiler import profile


class Solution:
  @profile
  def canTraverseAllPairs(self, nums: list[int]) -> bool:
    n_lists = 0 # unique, to always have unique keys
    dict_of_queue: dict[int, deque[int]] = {}  # try with different stuff # TODO change to list somewhow
    for num in nums:
      start_joining_key: int | None = None
      keys_to_delete: list[int] = [] # dictionary cant chang size during iteration
      for key, queue in dict_of_queue.items():
        if start_joining_key is None:
          for val in queue:
            if gcd(num, val) != 1:
              # join the list
              queue.append(num)
              # one matched and joined the set
              # so check for others to join this one
              start_joining_key = key
              break  # !!the optmization
        else:  # already found a match
          for val in queue:
            if gcd(num, val) != 1:
              # currently joining so it'll join the sets, and delete the latter from the list
              dict_of_queue[start_joining_key] += queue
              keys_to_delete.append(key)
              break
      for key in keys_to_delete:
        del dict_of_queue[key]
      if start_joining_key is None:  # if it's still none it's a new set:
        dict_of_queue[n_lists] = deque([num])
        n_lists += 1
    return len(dict_of_queue) == 1

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


if __name__ == "__main__":
  sol = Solution()
  sol.test()
  print("All tests passed!")
