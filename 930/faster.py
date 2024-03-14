from more_itertools import windowed_complete, windowed

class Solution:
  def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
    ret = 0
    # get indexes of 1
    indexes = [i for i in range(len(nums)) if nums[i] == 1]
    if len(indexes) < goal: return 0
    if goal == 0:
      if len(indexes) == 0: return self.sum_1_to_n(len(nums)) # no 1s
      # add extra magic indexes so window works
      if indexes[0] != 0: # first number is 0
        indexes.insert(0, -1)
      if indexes[-1] != len(nums) - 1: # last number is also 0
        indexes.append(len(nums))
      ret = 0
      for window in windowed(indexes, 2):
        ret += self.sum_1_to_n(window[1] - window[0] - 1) # big - (small + 1)
      return ret
    window: tuple; bef: tuple; after: tuple
    for bef, window, after in windowed_complete(indexes, goal):
      # logic: [0,0,1,0,0,1,0,0,0], goal: 2
      # [1,0,0,1]  , [0,1,0,0,1],   [0,0,1,0,0,1]: number of left 0s + 1
      # [1,0,0,1,0], [0,1,0,0,1,0], [0,0,1,0,0,1,0]: number of left 0s + 1, again
      # same thing for the rest, so it's number of right 0s + 1 (the first one)
      # results in (number of left 0s + 1) * (number of right 0s + 1)
      first1_i = window[0]
      last1_i = window[-1]
      n_0sBef = first1_i - bef[-1] - 1 if len(bef) > 0 else first1_i
      n_0sAft = after[0] - last1_i - 1 if len(after) > 0 else len(nums) - 1 - last1_i
      ret += (n_0sBef + 1) * (n_0sAft + 1)
    return ret
  def sum_1_to_n(self, n):
    return n * (n + 1) // 2
    # return sum(range(n + 1))
  def test(self):
    from icecream import ic
    assert ic(self.numSubarraysWithSum([1,0,1,0,1], 2)) == 4
    assert ic(self.numSubarraysWithSum([0,0,0,0,0], 0)) == 15
    assert ic(self.numSubarraysWithSum([0,1,1,1,1], 3)) == 3
    assert ic(self.numSubarraysWithSum([0,0,0,0,0,0,1,0,0,0], 0)) == 27

if __name__ == '__main__':
  s = Solution()
  s.test()
  print('pass')