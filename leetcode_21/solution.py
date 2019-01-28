# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def list(self):
        a, p = [], self
        while p:
            a.append(p.val)
            p = p.next
        return a

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 or l2

        head = ListNode(-1)
        
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        
        return head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)
    
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)

    print(l1.list())
    print(l2.list())
    print(Solution().mergeTwoLists(l1, l2).list())
