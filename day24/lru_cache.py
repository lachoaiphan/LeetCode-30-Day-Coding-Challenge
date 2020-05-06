"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.
"""

# Designed a LRU Cache with a hash table with the respective keys and values along with another data structure to keep track of the
# keys that are being recently used. O(n) time for each operations.


class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.access = []

    def get(self, key):
        if key in self.cache:
            self.access.append(self.access.pop(self.access.index(key)))
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.access.pop(self.access.index(key))
        elif len(self.cache) == self.capacity:
            first = self.access.pop(0)
            del self.cache[first]
        self.cache[key] = value
        self.access.append(key)
