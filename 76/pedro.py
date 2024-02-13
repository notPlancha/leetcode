from collections import defaultdict

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    altered: bool = False
    result: str = s
    tempRes:str
    t_dictionary = defaultdict(int)

    for char in t:
      t_dictionary[char] += 1

    for index in range(len(s)):
      t_dictionary_temp = t_dictionary.copy()

      if t_dictionary_temp[s[index]] > 0:

        if len(s) - index < len(t):
          break

        tempRes = ''

        for indexRes in range(index, len(s)):
          tempRes += s[indexRes]
          if t_dictionary_temp[s[indexRes]] > 0:
            t_dictionary_temp[s[indexRes]] -= 1

          valid = True
          for k in t_dictionary_temp:
            if t_dictionary_temp[k] > 0:
              valid = False
              break

          if valid:
            altered = True
            if len(tempRes) < len(result):
              result = tempRes

    if altered:
      return result
    else:
      return ''