from itertools import permutations
class Solution:
  def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
    ret = 0
    for perm in permutations(tokens):
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
    if power > token:
      power -= token
      score += 1
    elif score >= 1:
      power += token
      score -= 1
    else:
      raise StopIteration
    return power, score
  def test(self):
    from icecream import ic
    tokens = [100, 200, 300, 400]
    power = 200
    assert ic(self.bagOfTokensScore(tokens, power)) == 2
if __name__ == '__main__':
  s = Solution()
  s.test()
  print('All passed')