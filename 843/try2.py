from icecream import ic

from collections import Counter, defaultdict
from typing import NewType, Iterable, Iterator, Dict, List, Tuple
from sortedcontainers import SortedList
from more_itertools import peekable
from dataclasses import dataclass
letter = str
Word = str
count = int
@dataclass
class IterVal:
  it: Iterator[tuple[letter, count]]
  val: tuple[letter, count] | None
  i: int
  def __next__(self):
    self.val = next(self.it, None)
    return self.val
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


class SortedDictOnLen:
  def __init__(self, d: dict[letter, list[Word]]):
    self.list: SortedList[tuple[letter, list[Word]]] = SortedList(d.items(), key=lambda x: -len(x[1]))
    self.d = d
  def nth(self, n):
    return self.list[n]
  def __getitem__(self, item):
    return self.d[item]
  def __repr__(self):
    return repr(self.list)

class Solution:
  order_list: list[IterVal]
  dicts: dict[int, list[tuple[letter, count]]]
  def findSecretWord(self, words: list[str], master: "Master") -> None:
    words_set = set(words)
    self.generate_dicts(words)
    # get first word
    word_to_guess = ""
    for i in self.order_list:
      word_to_guess += i.val[0]
    while True:
      if word_to_guess in words_set:
        result = master.guess(word_to_guess)
      else:
        raise NotImplementedError
  def generate_dicts(self, words: list[Word]) -> None:
    self.dicts = {}
    for i in range(6):
      toDict = Counter(word[i] for word in words)
      self.dicts[i] = toDict.most_common()
    self.order_list: list[IterVal] = []
    for i, tups in self.dicts.items():
      self.order_list.append(IterVal(it = (g:= peekable(tups)), val = next(g, None), i = i))

  def iterate_order(self) -> Iterator[tuple[int, letter]]:
    while True:
      m: IterVal = max(self.order_list, key=lambda x: x.val[1])
      yield m.i, m.val[0]
      val = next(m)
      # if none
    #start_on = max(c for )

if __name__ == '__main__':
  s = Solution()
  s.findSecretWord(["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"], Master("hbaczn", 10))

  # s.findSecretWord(["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"], Master("ccoyyo", 10))
  print("Passed!")