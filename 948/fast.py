from icecream import ic

class Solution:
  def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
    tokens.sort()
    i_start, i_end = 0, len(tokens) - 1
    score = ret = 0
    while i_start <= i_end:
      if power >= tokens[i_start]:
        # take from start
        score += 1
        power -= tokens[i_start]
        # ic(i_start, tokens[i_start], score, power)
        i_start += 1
        if score > ret:
          ret = score
      else:
        # take from end
        if score == 0: return 0
        score -= 1
        power += tokens[i_end]
        # ic(i_end, tokens[i_end], score, power)
        i_end -= 1
    return ret
  def test(self):
    assert ic(self.bagOfTokensScore( [100, 200, 300, 400], 200)) == 2
    assert ic(self.bagOfTokensScore( [200,100], 150)) == 1
    assert ic(self.bagOfTokensScore( [100], 50)) == 0
    assert ic(self.bagOfTokensScore( [52,65,35,88,28,1,4,68,56,95], 94)) == 5
    assert ic(self.bagOfTokensScore( [71,55,82], 54)) == 0
if __name__ == '__main__':
  s = Solution()
  s.test()
  print('All passed')