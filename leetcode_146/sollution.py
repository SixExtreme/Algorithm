from collections import OrderedDict
from typing import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.ordered_dict: OrderedDict[int, int] = OrderedDict()


    def get(self, key: int) -> int:
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
        return self.ordered_dict.get(key, -1)


    def put(self, key: int, value: int):
        self.ordered_dict[key] = value
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
        if len(self.ordered_dict) > self.capacity:
            self.ordered_dict.popitem(last=False)
        



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