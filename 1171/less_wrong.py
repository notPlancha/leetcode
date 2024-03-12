from icecream import ic

from typing import Optional, Iterator
from more_itertools import windowed_complete

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  @staticmethod
  def from_list(li) -> Optional["ListNode"]:
    ret = current = ListNode()
    for i in li:
      current.next = ListNode(i)
      current = current.next
    return ret.next
  def __eq__(self, other):
    if other is None:
      return False
    return self.val == other.val and self.next == other.next
  def __hash__(self):
    return id(self) #not a real hash
  def __repr__(self):
    return f"{self.val}->{self.next}"

class Solution:
  def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # transform into list
    i = 1
    try:
      while True:
        for bef, nodes, after in windowed_complete(self.iter_LL(head), i):
          if len(nodes) == 0: return head
          if sum([node.val for node in nodes]) == 0:
            i -= 1
            if nodes[0] is head:
              head = nodes[-1].next
            else:
              bef[-1].next = nodes[-1].next
            break
        i += 1
    except ValueError:
      return head

  def iter_LL(self, head) -> Iterator[ListNode]:
    while True:
      if head is not None:
        yield head
      else:
        return
      head = head.next
  def index_of_ll(self, head, i):
    for _ in range(i):
      head = head.next
    return head
  def test(self):
    from icecream import ic
    assert ic(self.removeZeroSumSublists(ListNode.from_list([1,2,-3,3,1]))) in [ListNode.from_list([3,1]), ListNode.from_list([1,2,1])]
    assert ic(self.removeZeroSumSublists(ListNode.from_list([1,2,3,-3,4]))) == ListNode.from_list([1,2,4])
    assert ic(self.removeZeroSumSublists(ListNode.from_list([1,2,3,-3,-2]))) == ListNode.from_list([1])
    assert ic(self.removeZeroSumSublists(ListNode.from_list([0,0]))) == ListNode.from_list([])
    assert ic(self.removeZeroSumSublists(ListNode.from_list([1,2,1,-2,0,0]))) == ListNode.from_list([1,2,1,-2])


if __name__ == '__main__':
  s = Solution()
  s.test()
  print("Tests passed")