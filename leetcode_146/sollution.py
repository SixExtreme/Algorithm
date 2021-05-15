from collections import OrderedDict
from typing import OrderedDict


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity: int = capacity
#         self.ordered_dict: OrderedDict[int, int] = OrderedDict()


#     def get(self, key: int) -> int:
#         if key in self.ordered_dict:
#             self.ordered_dict.move_to_end(key)
#         return self.ordered_dict.get(key, -1)


#     def put(self, key: int, value: int):
#         self.ordered_dict[key] = value
#         if key in self.ordered_dict:
#             self.ordered_dict.move_to_end(key)
#         if len(self.ordered_dict) > self.capacity:
#             self.ordered_dict.popitem(last=False)

class ListNode:

    def __init__(self, key: int, value: int, prev=None, next=None):
        self.key = key
        self.value: int = value
        self.prev: ListNode = prev
        self.next: ListNode = next

class LinkList:

    def __init__(self):
        self.head: ListNode = ListNode(-1, -1)
        self.tail: ListNode = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node: ListNode):
        prev = self.tail.prev
        prev.next, self.tail.prev = node, node
        node.prev, node.next = prev, self.tail

    def popleft(self) -> ListNode:
        if self.head.next is self.tail:
            return None
        node = self.head.next
        self.head.next, node.next.prev = node.next, self.head
        return node

    def delete(self, node: ListNode):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def to_list(self):
        curr, values = self.head.next, []
        while curr is not self.tail:
            values.append(curr.value)
            curr = curr.next
        return values

class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.map = dict()
        self.linklist = LinkList()
    
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node: ListNode = self.map[key]
        self.linklist.delete(node)
        self.linklist.append(node)
        return node.value

    def put(self, key: int, value: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.linklist.delete(node)
        
        node = ListNode(key, value)
        self.map[key] = node
        self.linklist.append(node)
        
        if len(self.map) > self.capacity:
            node = self.linklist.popleft()
            del self.map[node.key]


# Your LRUCache object will be instantiated and called as such:
if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))