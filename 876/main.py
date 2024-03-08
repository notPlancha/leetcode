
from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    head1 = head
    head2 = head
    while True:
      if head2.next is None:
        return head1
      if head2.next.next is None:
        return head1.next
      head1 = head1.next
      head2 = head2.next.next