from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1
        self.lru_cache.move_to_end(key)
        return self.lru_cache[key]        

    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
            self.lru_cache.move_to_end(key)
        self.lru_cache[key] =  value
        
        if len(self.lru_cache) > self.capacity:
            self.lru_cache.popitem(last=False)
