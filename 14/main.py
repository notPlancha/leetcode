class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    ret = ""
    first = strs[0]
    rest = strs[1:]
    try:
      for i in range(len(first)):
        curr = first[i]
        for j in rest:
          if curr != j[i]:
            break
        else:
          ret += curr
          continue
        break
    except IndexError:
      return ret
    return ret