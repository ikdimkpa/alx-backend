#!/usr/bin/env python3
"""Defines a class LRUCache"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Inherits from BaseCaching"""
    def __init__(self):
        """Initializes an object"""
        super().__init__()
        self.fifo_queue = deque()

    def put(self, key, item):
        """Setter Method"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and\
                    key not in self.cache_data:
                discarded_key = self.fifo_queue.popleft()
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            elif key in self.cache_data:
                self.fifo_queue.remove(key)

            self.cache_data[key] = item
            self.fifo_queue.append(key)

    def get(self, key):
        """Getter Method"""
        if key in self.cache_data:
            self.fifo_queue.remove(key)
            self.fifo_queue.append(key)
        return self.cache_data.get(key, None)
