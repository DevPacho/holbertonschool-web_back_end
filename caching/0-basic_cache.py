#!/usr/bin/python3
""" Basic dictionary to caching """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system """

    def put(self, key, item):
        """ Assigns an item to the cache dictionary """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ Returns an item from the cache dictionary linked to a key """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
