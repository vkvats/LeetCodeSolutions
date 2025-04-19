class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = set()
        self.key_values = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key not in self.keys:
            self.keys.add(key)
            self.key_values.append([key, value])
        else:
            for pair in self.key_values:
                if pair[0] == key:
                    pair[1] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.keys:
            for pair in self.key_values:
                if pair[0] == key: return pair[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.keys:
            value = self.get(key)
            self.key_values.remove([key, value])
            self.keys.remove(key)

