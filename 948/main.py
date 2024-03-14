from icecream import ic

from more_itertools import distinct_permutations
class Solution:
  def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
    ret = 0
    for i in range(1, len(tokens) + 1):
      for perm in distinct_permutations(tokens, r=i):
        try:
          currPower = power
          score = 0
          for token in perm:
            currPower, score = self.play(token, currPower, score)
          if score > ret: ret = score
        except StopIteration:
          continue
    return ret
  def play(self, token, power, score) -> tuple[int, int]:
    if power >= token:
      power -= token
      score += 1
    elif score >= 1:
      power += token
      score -= 1
    else:
      raise StopIteration
    return power, score
  def test(self):
    assert ic(self.bagOfTokensScore( [100, 200, 300, 400], 200)) == 2
    assert ic(self.bagOfTokensScore( [200,100], 150)) == 1
    assert ic(self.bagOfTokensScore( [100], 50)) == 0
    ic(self.bagOfTokensScore( [52,65,35,88,28,1,4,68,56,95], 94))
if __name__ == '__main__':
  s = Solution()
  s.test()
  print('All passed')