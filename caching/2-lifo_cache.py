#!/usr/bin/env python3
""" LIFO algorithm to caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Calling parent init """
        super().__init__()

    def put(self, key, item):
        """ Assigns an item to the cache dictionary """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lastItem = list(self.cache_data.keys())[-2]
            self.cache_data.pop(lastItem)

            print("DISCARD:", lastItem)

    def get(self, key):
        """ Returns an item from the cache dictionary linked to a key """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
