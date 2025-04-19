class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.arr:
            self.arr.add(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.arr:
            self.arr.remove(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return sample(self.arr, 1)[0]

# solution from leetcode
