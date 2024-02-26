"""
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can
traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest
common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of
traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.
"""

from icecream import ic
from line_profiler import profile

from math import gcd
from collections import deque


class Solution:
  @profile
  def canTraverseAllPairs(self, nums: list[int]) -> bool:
    list_of_queues: list[list[int | deque[int]] | None] = []  # list(tuple(key, queue)) # ignore is used so the gc doesn't pickup the deque
    for num in nums:
      start_joining_key: int | None = None
      for queue_t in list_of_queues:
        if queue_t is None: continue
        if start_joining_key is None:
          for val in queue_t[1]:
            if gcd(num, val) != 1:
              # join the list
              queue_t[1].append(num)
              # one matched and joined the set
              # so check for others to join this one
              start_joining_key = queue_t[0]
              break  # !!the optmization
        else:  # already found a match
          for val in queue_t[1]:
            if gcd(num, val) != 1:
              # currently joining so it'll join the sets, and delete the latter from the list
              list_of_queues[start_joining_key][1] += queue_t[1]
              list_of_queues[queue_t[0]] = None
              break
      del_keys = []
      if start_joining_key is None:  # if it's still none it's a new set:
        new_queue = deque()
        new_queue.append(num)
        list_of_queues.append([
          len(list_of_queues), new_queue
        ])
    return sum(1 for i in list_of_queues if i is not None) == 1

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
