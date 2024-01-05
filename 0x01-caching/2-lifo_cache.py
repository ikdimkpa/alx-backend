#!/usr/bin/env python3
"""Defines a class"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching"""
    def __init__(self):
        """Unitializes an object"""
        super().__init__()
        self.fifo_queue = deque()

    def put(self, key, item):
        """Setting Method"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                discarded_key = self.fifo_queue.pop()
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.fifo_queue.append(key)

    def get(self, key):
        """Getting Method"""
        return self.cache_data.get(key, None)
