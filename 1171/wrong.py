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
class Solution:
  def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    M: list[tuple[ListNode, list[int]]] = []
    for node in self.iter_LL(head):
      M.append((node, [node.val]))
      foundZero, n_to_remove = False, 0
      for l in reversed(M[:-1]):
        n_to_remove += 1
        toAdd = l[1][-1] + node.val
        if toAdd == 0:
          foundZero = True
          break
        l[1].append(toAdd)
      # a         b       ~c~      ~d~   ~e~ f
      # a+b       ~b+c~   ~c+d~    ~d+e~
      # ~a+b+c~   ~b+c+d~ ~c+d+e~
      # ~a+b+c+d~ b+f
      # a+b+f                               c+d+e = 0
      if foundZero:
        # remove last n that included 0 sum
        for _ in range(n_to_remove):
          del M[-1]
        # fix linkedlist
        M[-1][0].next = node.next
        # finally remove from matrix those that used the removed
        for l in M:
          for _ in range(n_to_remove - 1):
            del l[1][-1]
    return M[0][0]
  def iter_LL(self, head) -> Iterator[ListNode]:
    while True:
      if head:
        yield head
      else:
        return
      head = head.next