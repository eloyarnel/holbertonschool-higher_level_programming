#!/usr/bin/env python3
"""
Provides an iterator wrapper that counts how many items
have been iterated over.
"""


class CountedIterator:
    """Iterator that counts the number of items returned."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)   # may raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count
