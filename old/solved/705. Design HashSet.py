class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [] # can also use set() here

    def add(self, key: int) -> None:
        if key not in self.hash:
            self.hash.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hash:
            return True
        else:
            return False

