#!/usr/bin/env python3
"""Derfines a class BasicCache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Caching System"""

    def __init__(self):
        """Initializes class attribute"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns an item via the key"""
        return self.cache_data.get(key, None)
