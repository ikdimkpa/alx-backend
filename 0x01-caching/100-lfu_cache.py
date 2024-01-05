#!/usr/bin/env python3
"""Defines a class LFUCache"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Inherits from BaseCaching"""
    def __init__(self):
        """Initializes an object"""
        super().__init__()
        self.freq_record = {}

    def put(self, key, item):
        """Setter Method"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                discarded_key = min(self.freq_record, key=self.freq_record.get)
                del self.freq_record[discarded_key]
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            if key in self.freq_record:
                self.freq_record[key] += 1
            else:
                self.freq_record[key] = 1

    def get(self, key):
        """Getter Method"""
        if key in self.freq_record:
            self.freq_record[key] += 1
        return self.cache_data.get(key, None)
