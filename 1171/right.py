from typing import Optional, Iterator

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

def nodes(head) -> Iterator[ListNode]:
  while True:
    if head is not None:
      yield head
    else:
      return
    head = head.next

class Solution:
  def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    ret = curr = ListNode()
    while True:
      skip = False
      s = 0
      for node in nodes(head):
        s += node.val
        if s == 0:
          skip = True
          break
      if skip:
        head = node.next
      else:
        curr.next = ListNode(head.val)
        curr = curr.next
        head = head.next
      if head is None:
        return ret.next
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
