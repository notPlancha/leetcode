# Definition for singly-linked list.
# cnextlass ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    h = list1
    for i in range(a-1):
        h = h.next
    t = h.next
    for j in range(b-a):
        t = t.next
    g = list2
    while g.next is not None:
        g = g.next
    h.next = list2
    g.next = t.next
    return list1