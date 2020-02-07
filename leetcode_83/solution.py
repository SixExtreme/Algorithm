# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        vals = []
        p = self
        while p:
            vals.append(p.val)
            p = p.next
        return vals


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # import ipdb; ipdb.set_trace()
        p = head
        while p:
            q = p.next
            while q and q.val == p.val:
                q = q.next
            p.next = q
            p = p.next
        return head


def test_solution():
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(2)
    assert Solution().deleteDuplicates(head1).to_list() == [1, 2]

    # head2 = ListNode(1)
    # head2.next = ListNode(1)
    # head2.next.next = ListNode(2)
    # head2.next.next.next = ListNode(3)
    # head2.next.next.next.next = ListNode(3)
    # assert Solution().deleteDuplicates(head2).to_list() == [1, 2, 3]
