# Definition for singly-linked list.
from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  def __repr__(self):
    return f"({self.val}) -> {self.next}"
  def __eq__(self, other):
    if not isinstance(other, ListNode):
      return False
    if self.val != other.val:
      return False
    return self.next == other.next
  @staticmethod
  def fromList(li) -> Optional["ListNode"]:
    ret = current = ListNode()
    for i in li:
      current.next = ListNode(i)
      current = current.next
    return ret.next
class Solution:
  def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode:
    ret = current = ListNode()
    if list1 is None: return list2
    if list2 is None: return list1
    while True:
      list1, list2 = (list1, list2) if list1.val < list2.val else (list2, list1)
      current.next = list1
      current = current.next
      if current.next is None:
        # append list2
        current.next = list2
        return ret.next
      list1 = list1.next
  def test(self):
    from icecream import ic
    assert ic(self.mergeTwoLists(
      ListNode.fromList([1,2,4]),
      ListNode.fromList([1,3,4])
    )) == ListNode.fromList([1,1,2,3,4,4])
    assert ic(self.mergeTwoLists(
      ListNode.fromList([]),
      ListNode.fromList([])
    )) == ListNode.fromList([])
    assert ic(self.mergeTwoLists(
      ListNode.fromList([]),
      ListNode.fromList([0])
    )) == ListNode.fromList([0])

if __name__ == "__main__":
  sol = Solution()
  sol.test()
  print("All tests passed!")