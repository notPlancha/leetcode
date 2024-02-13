"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

"""
O plano e expandir e contract da esquerda pra direita
"""
from collections import deque, Counter
from line_profiler import profile

class Solution:
  @profile
  def minWindow(self, s: str, t: str) -> str:
    ret: deque | None = None
    mainQueue = deque(maxlen=len(s))
    t_counter = Counter(t)
    t_len = len(t)
    curr_str_counter = Counter()
    for i in s:
      # expand
      mainQueue.append(i)
      if i in t_counter:
        curr_str_counter[i] += 1
        if curr_str_counter >= t_counter: # this can be otpimized because it's comparing already compared (only first time?)
          # contract then save if useful
          self.contract(mainQueue, curr_str_counter, t_counter)
          ret = min(ret, mainQueue.copy(), key=len) if ret is not None else mainQueue.copy() # if I used indices it would be way faster
    return "".join(ret) if ret is not None else ""
  @profile
  def contract(self, curr_queue: deque, curr_counter: Counter, t_counter: Counter):
    while True:
      val = curr_queue.popleft()
      # cannot be less
      if val in t_counter:
        if curr_counter[val] == t_counter[val]:
          # can't contract anymore
          curr_queue.appendleft(val) # reput the value
          return
        else:
          curr_counter[val] -= 1
  def test(self):
      from icecream import ic
      assert ic(self.minWindow("ADAOBECODEBANC", "ABC")) == "BANC"
      assert ic(self.minWindow("ADOBECODEBANCFBC", "ABC")) == "BANC"
      assert ic(self.minWindow("ADBOBECODEBANCFBC", "ABC")) == "BANC"
      assert ic(self.minWindow("a", "a")) == "a"
      assert ic(self.minWindow("a", "aa")) == ""
if __name__ == "__main__":
  s = Solution()
  s.test()
  print("All tests passed!")