class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        c = head

        while c is not None:
            n = c.next
            c.next = p
            p = c
            c = n

        return p