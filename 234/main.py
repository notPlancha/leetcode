# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
#
#
#  Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
#  Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [1, 10⁵].
#  0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in
# O(n) time and
# O(1) space?
#
#  Related Topics Linked List Two Pointers Stack Recursion 👍 16086 👎 866
from icecream import ic
from typing import Optional
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
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # find middle
    if head.next is None: return True # len 1
    if head.next.next is None: return head.val == head.next.val # len 2
    fast = curr = head
    prev = None
    while True:
      fast = fast.next.next
      nextt = curr.next
      curr.next = prev
      if fast.next is None:
        # impar
        l1 = curr
        l2 = nextt.next
        break
      elif fast.next.next is None:
        # par
        l1 = nextt
        l2 = nextt.next
        nextt.next = curr
        break
      prev = curr
      curr = nextt

    while l1 is not None:
      if l1.val != l2.val: return False
      l1 = l1.next
      l2 = l2.next
    return True

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
  assert ic(Solution().isPalindrome(ListNode.from_list([1,2,2,1]))) is True
  assert ic(Solution().isPalindrome(ListNode.from_list([1,2]))) is False
  assert ic(Solution().isPalindrome(ListNode.from_list([1,2,3,2,1]))) is True
  assert ic(Solution().isPalindrome(ListNode.from_list([1,2,3,3,2,1]))) is True
  assert ic(Solution().isPalindrome(ListNode.from_list([1,0,1]))) is True
  assert ic(Solution().isPalindrome(ListNode.from_list([1,0,0]))) is False
  assert ic(Solution().isPalindrome(ListNode.from_list([1,2,3,4]))) is False