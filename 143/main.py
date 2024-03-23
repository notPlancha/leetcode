# You are given the head of a singly linked-list. The list can be represented
# as:
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
#  Reorder the list to be on the following form:
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#
#  You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
#
#
#  Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
#
#  Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [1, 5 * 10⁴].
#  1 <= Node.val <= 1000
#
#
#  Related Topics Linked List Two Pointers Stack Recursion 👍 10729 👎 380
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  @staticmethod
  def from_list(l):
    head = None
    for i in reversed(l):
      head = ListNode(i, head)
    return head
  def __repr__(self):
    return f"{self.val} -> {self.next}"
  def __eq__(self, other):
    return str(self) == str(other)
from typing import Optional
from icecream import ic
# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    temp = head
    rev, count = self.reversedList(head)
    if count % 2 == 0:
      for node in rev:
        hn = head.next
        if hn is node:
          head.next = hn
          hn.next = None
          break
        head.next = node
        node.next = hn
        head = hn
    else:
      for node in rev:
        hn = head.next
        if head is node:
          head.next = None
          break
        head.next = node
        node.next = hn
        head = hn
  def reversedList(self, head: Optional[ListNode]):
    ret = deque()
    ret.appendleft(head)
    i = 1
    while head.next is not None:
      i += 1
      head = head.next
      ret.appendleft(head)
    return ret, i
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
  headd = ListNode.from_list([1,2,3,4,5,6,7])
  Solution().reorderList(headd)
  ic(headd)