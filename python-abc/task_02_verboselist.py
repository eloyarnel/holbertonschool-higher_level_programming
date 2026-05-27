#!/usr/bin/env python3
"""
Extends the built-in list class to provide notifications
when items are added or removed.
"""


class VerboseList(list):
    """Custom list that prints messages on modifications."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

3) #!/usr/bin/env python3
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
