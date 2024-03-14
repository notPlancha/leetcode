from typing import Iterable

from icecream import ic

from itertools import combinations, product
class Master:
  def __init__(self, master_word, guesses):
    self.master_word = master_word
    self.guesses = guesses
  def guess(self, word: str) -> int:
    ic(word)
    self.guesses -= 1
    if self.guesses < 0:
      raise AssertionError("No more guesses, stopped on " + word + ", dind't reach " + self.master_word)
    ret = 0
    for i in range(len(word)):
      if word[i] == self.master_word[i]:
        ret += 1
    if ret == len(self.master_word):
      raise StopIteration("Guessed it!")
    return ret

class Solution:
  l = [0,1,2,3,4,5]
  imp_set = {i: set() for i in range(6)}
  # l1 = combinations(l, 1)
  # l2 = combinations(l, 2)
  # l3 = combinations(l, 3)
  # l4 = combinations(l, 4)
  # l5 = combinations(l, 5)
  def findSecretWord(self, words: list[str], master: "Master") -> None:
    # first
    first_result = master.guess(words[0])
    matches = self.from_word(words[0], first_result)
    list_of_non_matches = set()
    for word in words[1:]:
      if self.is_word_impossible(word): continue
      if any(self.is_compatible(word, match) is not None for match in matches):
        result = master.guess(word)
        if result == 0:
          self.add_to_imp_set(word)
          continue
        result_matches = self.from_word(word, result)
        matches = self.join_compatible(matches, result_matches)
        if len(matches) == 0: raise Exception
  def from_word(self, word: str, matches: int) -> list[Iterable[str]]:
    perms = combinations(self.l[:len(word)], matches) # TODO change to only 6
    ret = []
    for perm in perms:
      # ic(perm, word[perm[0]], word[perm[1]])
      to_add = [
        word[i] if i in perm else "_"
        for i in range(len(word))
      ]
      ret.append(to_add)
    return ret
  def is_compatible(self, iter1: Iterable[str], iter2: Iterable[str]) -> Iterable[str] | None:
    ret = []
    for i in zip(iter1, iter2):
      if "_" in (l := sorted(i)) or i[0] == i[1]:
        ret.append(l[-1])
      else:
        return None
    return ret
  def join_compatible(self, matches1: list[Iterable[str]], matches2: list[Iterable[str]]) -> list[Iterable[str]]:
    ret = []
    for match1 in matches1:
      for match2 in matches2:
        if (joined := self.is_compatible(match1, match2)) is not None:
          ret.append(joined)
    return ret
  def add_to_imp_set(self, word):
    for i in range(6):
      self.imp_set[i].add(word[i])
  def is_word_impossible(self, word):
    for i in range(6):
      if word[i] in self.imp_set[i]:
        return True
    return False
  def print_compatible(self, matches1, matches2):
    for match1 in matches1:
      for match2 in matches2:
        ic(match1, match2, self.is_compatible(match1, match2))

if __name__ == '__main__':
  s = Solution()
  # ic(s.from_word("abcdef", 3))
  # s.print_compatible(s.from_word("abd", 2), s.from_word("dbc", 2))
  # s.print_compatible(s.from_word("abdj", 2), s.from_word("dbcj", 2))
  try:
    s.findSecretWord(["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"], Master("hbaczn", 10))
  except StopIteration:
    print("Passed 1")
  try:
    s.findSecretWord(["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"], Master("ccoyyo", 10))
  except StopIteration:
    print("Passed 2")
  print("Passed!")