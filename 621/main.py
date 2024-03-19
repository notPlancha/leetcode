# You are given an array of CPU tasks, each represented by letters A to Z, and
# a cooling time, n. Each cycle or interval allows the completion of one task.
# Tasks can be completed in any order, but there's a constraint: identical tasks must
# be separated by at least n intervals due to cooling time.
#
#  Return the minimum number of intervals required to complete all tasks.
#
#
#  Example 1:
#
#
#  Input: tasks = ["A","A","A","B","B","B"], n = 2
#
#
#  Output: 8
#
#  Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A ->
#  B.
#
#  After completing task A, you must wait two cycles before doing A again. The
# same applies to task B. In the 3ʳᵈ interval, neither A nor B can be done, so you
# idle. By the 4ᵗʰ cycle, you can do A again as 2 intervals have passed.
#
#  Example 2:
#
#
#  Input: tasks = ["A","C","A","B","D","B"], n = 1
#
#
#  Output: 6
#
#  Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
#
#  With a cooling interval of 1, you can repeat a task after just one other
# task.
#
#  Example 3:
#
#
#  Input: tasks = ["A","A","A", "B","B","B"], n = 3
#
#
#  Output: 10
#
#  Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B ->
# idle -> idle -> A -> B.
#
#  There are only two types of tasks, A and B, which need to be separated by 3
# intervals. This leads to idling twice between repetitions of these tasks.
#
#
#  Constraints:
#
#
#  1 <= tasks.length <= 10⁴
#  tasks[i] is an uppercase English letter.
#  0 <= n <= 100
#
#
#  Related Topics Array Hash Table Greedy Sorting Heap (Priority Queue)
# Counting 👍 9767 👎 2002

from icecream import ic
# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter, deque
from sortedcontainers import SortedList

class Solution:
  def leastInterval(self, tasks: list[str], n: int) -> int:
    c: SortedList[tuple[int, str]] = SortedList(((count, task) for task, count in Counter(tasks).most_common()), key=lambda x: -x[0])
    seq: deque = deque([None for _ in range(n)])
    set_of_seq = set()
    ret = 0
    while True:
      # ic(c, seq)
      if len(c) == 0: return ret
      for i in range(len(c)):
        count, task = c[i]
        if task not in set_of_seq:
          # ic(ret, count, task)
          count -= 1
          seq.append(task)
          set_of_seq.add(task)
          if count > 0:
            c.add((count, task))
          del c[i]
          break
      else:
        # ic(ret, "idle")
        seq.append(None)
      ret += 1
      to_rem = seq.popleft()
      if to_rem is not None: set_of_seq.remove(to_rem)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
  s = Solution()
  assert ic(s.leastInterval(["A","A","A","B","B","B"], 2)) == 8
  assert ic(s.leastInterval(["A","C","A","B","D","B"], 1)) == 6
  assert ic(s.leastInterval(["A","A","A", "B","B","B"], 3)) == 10
  ic.enable()
  assert ic(s.leastInterval(["A","B","C","D","E","A","B","C","D","E"], 4)) == 10