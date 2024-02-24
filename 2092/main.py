"""
You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.

Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.

The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.
"""

from collections import defaultdict


def join_meetings(meetings: list[set]) -> list[set]:
  # [{1,2}, {2,3}, {4,5}] -> [{1,2,3}, {4,5}]
  # [{1, 3}, {0, 2}, {2, 3}] -> [{1,3,2,0}]
  ret = [meetings[0].copy()]
  for meeting in meetings:
    for i in ret:
      if i.intersection(meeting):
        i.update(meeting)
        break
    else:  # doesn't go to else if for breaks
      ret.append(meeting.copy())
  if meetings == ret: return ret
  else: return join_meetings(ret)


class Solution:
  def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> set[int]:
    ret = {0, firstPerson}
    # get times (desta forma se for ao mesmo tempo partilha para todos)
    horario: defaultdict[int, list] = defaultdict(list[set])  # time : meetings
    for meeting in meetings:
      horario[meeting[2]].append({meeting[0], meeting[1]})
    # share secrets
    for time, list_of_meetings in sorted(horario.items(), key=lambda tup: tup[0]):  # sort by time
      list_of_meetings = join_meetings(list_of_meetings)
      for meeting in list_of_meetings:
        if ret.intersection(meeting):  # can optimize this call prob
          ret.update(meeting)
    return ret

  def test(self):
    from icecream import ic
    assert ic(self.findAllPeople(
      6,
      [[1, 2, 5], [2, 3, 8], [1, 5, 10]],
      1
    )) == {0, 1, 2, 3, 5}
    assert ic(self.findAllPeople(
      4,
      [[3, 1, 3], [1, 2, 2], [0, 3, 3]],
      3
    )) == {0, 1, 3}
    assert ic(self.findAllPeople(
      5,
      [[3, 4, 2], [1, 2, 1], [2, 3, 1]],
      1
    )) == {0, 1, 2, 3, 4}
    assert ic(self.findAllPeople(  # at the same time issues
      5,
      [[1, 4, 3], [0, 4, 3]],
      3
    )) == {0, 1, 3, 4}
    assert ic(self.findAllPeople(  # people sharing the same time but different meetings
      6,
      [[0, 2, 1], [1, 3, 1], [4, 5, 1]],
      1
    )) == {0, 1, 2, 3}
    assert ic(self.findAllPeople(  # people sharing the same time but different meetings
      5,
      [[1, 3, 3], [2, 0, 3], [2, 3, 3]],
      4
    )) == {0, 1, 2, 3, 4}


if __name__ == "__main__":
  sol = Solution()
  sol.test()
  print("All tests passed!")