class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def gen(self, head: ListNode | None):
    while True:
      if head.next is None:
        return
      yield head.next
      head = head.next

  def hasCycle(self, head: ListNode | None) -> bool:
    if head is None: return False
    ret = []
    for curr in self.gen(head):
      if curr in ret:
        return True
      ret.append(curr)
    return False
