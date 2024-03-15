# You are given an array of unique strings words where words[i] is six letters
# long. One word of words was chosen as a secret word.
#
#  You are also given the helper object Master. You may call Master.guess(word)
# where word is a six-letter-long string, and it must be from words. Master.guess(
# word) returns:
#
#
#  -1 if word is not from words, or
#  an integer representing the number of exact matches (value and position) of
# your guess to the secret word.
#
#
#  There is a parameter allowedGuesses for each test case where allowedGuesses
# is the maximum number of times you can call Master.guess(word).
#
#  For each test case, you should call Master.guess with the secret word
# without exceeding the maximum number of allowed guesses. You will get:
#
#
#  "Either you took too many guesses, or you did not find the secret word." if
# you called Master.guess more than allowedGuesses times or if you did not call
# Master.guess with the secret word, or
#  "You guessed the secret word correctly." if you called Master.guess with the
# secret word with the number of calls to Master.guess less than or equal to
# allowedGuesses.
#
#
#  The test cases are generated such that you can guess the secret word with a
# reasonable strategy (other than using the bruteforce method).
#
#
#  Example 1:
#
#
# Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"],
# allowedGuesses = 10
# Output: You guessed the secret word correctly.
# Explanation:
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6
# matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
# We made 5 calls to master.guess, and one of them was the secret, so we pass
# the test case.
#
#
#  Example 2:
#
#
# Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
# Output: You guessed the secret word correctly.
# Explanation: Since there are two words, you can guess both.
#
#
#
#  Constraints:
#
#
#  1 <= words.length <= 100
#  words[i].length == 6
#  words[i] consist of lowercase English letters.
#  All the strings of wordlist are unique.
#  secret exists in words.
#  10 <= allowedGuesses <= 30
#
#
#  Related Topics Array Math String Interactive Game Theory 👍 1508 👎 1765
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

# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
from collections import Counter
class Solution:
  def findSecretWord(self, words: list[str], master: "Master") -> None:
    counters: list[Counter[letter]] = [Counter([word[i] for word in words]) for i in range(6)]
    pesos = {word: sum(counter[word[i]] for counter, i in zip(counters, range(6))) for word in words}
    pesos = dict(sorted(pesos.items(), key=lambda x: x[1], reverse=True))
    nono_sets = [set() for _ in range(6)]
    submited = set()
    for word in pesos.keys():
      if word in submited or any(word[i] in nono_sets[i] for i in range(6)): continue
      # do smth else if it's not enough here
      result = master.guess(word)
      submited.add(word)
      if result == 0:
        [nono_sets[i].add(word[i]) for i in range(6)]
      elif result == 6: return
      else:
        # add to submited those that don't have a match
        for word_ in words:
          c = 0
          for letter1, letter2 in zip(word, word_):
            if letter1 == letter2:
              c += 1
              if c == result:
                break
          else:
            submited.add(word_)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
  s = Solution()
  master = Master("ccoyyo", 10)
  s.findSecretWord(["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"], master)
  master = Master("vftnkr", 12)
  s.findSecretWord(["mjpsce","giwiyk","slbnia","pullbr","ezvczd","dwkrmt","qgzebh","wvhhlm","kqbmny","zpvrkz","pdwxvy","gilywa","gmrrdc","vvqvla","rmjirt","qmvykq","mhbmuq","unplzn","qkcied","eignxg","fbfgng","xpizga","twubzr","nnfaxr","skknhe","twautl","nglrst","mibyks","qrbmpx","ukgjkq","mhxxfb","deggal","bwpvsp","uirtak","tqkzfk","hfzawa","jahjgn","mteyut","jzbqbv","ttddtf","auuwgn","untihn","gbhnog","zowaol","feitjl","omtiur","kwdsgx","tggcqq","qachdn","dixtat","hcsvbw","chduyy","gpdtft","bjxzky","uvvvko","jzcpiv","gtyjau","unsmok","vfcmhc","hvxnut","orlwku","ejllrv","jbrskt","xnxxdi","rfreiv","njbvwj","pkydxy","jksiwj","iaembk","pyqdip","exkykx","uxgecc","khzqgy","dehkbu","ahplng","jomiik","nmcsfe","bclcbp","xfiefi","soiwde","tcjkjp","wervlz","dcthgv","hwwghe","hdlkll","dpzoxb","mpiviy","cprcwo","molttv","dwjtdp","qiilsr","dbnaxs","dbozaw","webcyp","vftnkr","iurlzf","giqcfc","pcghoi","zupyzn","xckegy"], master)
  master = Master("hbaczn", 10)
  s.findSecretWord(["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"], master)