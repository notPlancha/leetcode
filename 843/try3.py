from itertools import pairwise

from more_itertools import windowed
from icecream import ic
class Master:
  def __init__(self, master_word, guesses):
    self.master_word = master_word
    self.guesses = guesses
  def guess(self, word: str) -> int:
    self.guesses -= 1
    if self.guesses < 0:
      raise AssertionError("No more guesses, stopped on " + word + ", dind't reach " + self.master_word)
    ret = 0
    for i in range(len(word)):
      if word[i] == self.master_word[i]:
        ret += 1
    # if ret == len(self.master_word):
    #   raise StopIteration("Guessed it!")
    ic(self.master_word, word, ret)
    return ret



from collections import defaultdict

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
  def findSecretWord(self, words: list[str], master: "Master") -> None:
    words.sort()
    results = defaultdict(list)
    sets = [set() for i in range(6)] # create 6 sets of no nos
    submited = set()
    for i in range(len(words)):
      word = words[i]
      # check if nono or if it's repeated
      if word in submited or any(word[j] in sets[j] for j in range(6)): continue
      if len(results) == 0 or all(check_if_match(match, word, count) for count, matches in results.items() for match in matches):
        submited.add(word)
        result = master.guess(word)
        if result == 0:
          add_to_nono(word, sets)
        elif result == 6:
          return
        else:
          for j in range(len(results[result])):
            pair = word, results[result][j]
            if len(g:= where_is_match(*pair)) == result:
              new_match = ["_" if i not in g else pair[0][i] for i in range(6)]
              matches = [word_ for word_ in words[i:] if check_if_match(word_, new_match, result)]
              for match in matches:
                words.insert(i + 2, match)
          results[result].append(word)




def where_is_match(word1, word2) -> list[int]:
  i = -1
  ret = []
  for a,b in zip(word1, word2):
    i += 1
    if a == b:
      ret.append(i)
  return ret
def add_to_nono(word, sets):
  [sets[i].add(word[i]) for i in range(6)]
# words = np.array([list(i) for i in l], dtype="S1")

def check_if_match(word1, word2, times):
  ret = 0
  for char1, char2 in zip(word1, word2):
    if char1 == char2:
      ret += 1
      if ret >= times:
        return True
  return False

if __name__ == "__main__":
  s = Solution()
  master = Master("ccoyyo", 10)
  s.findSecretWord(["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"], master)
  master = Master("vftnkr", 12)
  s.findSecretWord(["mjpsce","giwiyk","slbnia","pullbr","ezvczd","dwkrmt","qgzebh","wvhhlm","kqbmny","zpvrkz","pdwxvy","gilywa","gmrrdc","vvqvla","rmjirt","qmvykq","mhbmuq","unplzn","qkcied","eignxg","fbfgng","xpizga","twubzr","nnfaxr","skknhe","twautl","nglrst","mibyks","qrbmpx","ukgjkq","mhxxfb","deggal","bwpvsp","uirtak","tqkzfk","hfzawa","jahjgn","mteyut","jzbqbv","ttddtf","auuwgn","untihn","gbhnog","zowaol","feitjl","omtiur","kwdsgx","tggcqq","qachdn","dixtat","hcsvbw","chduyy","gpdtft","bjxzky","uvvvko","jzcpiv","gtyjau","unsmok","vfcmhc","hvxnut","orlwku","ejllrv","jbrskt","xnxxdi","rfreiv","njbvwj","pkydxy","jksiwj","iaembk","pyqdip","exkykx","uxgecc","khzqgy","dehkbu","ahplng","jomiik","nmcsfe","bclcbp","xfiefi","soiwde","tcjkjp","wervlz","dcthgv","hwwghe","hdlkll","dpzoxb","mpiviy","cprcwo","molttv","dwjtdp","qiilsr","dbnaxs","dbozaw","webcyp","vftnkr","iurlzf","giqcfc","pcghoi","zupyzn","xckegy"], master)