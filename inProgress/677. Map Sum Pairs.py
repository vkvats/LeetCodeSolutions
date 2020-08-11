class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = {}

    def insert(self, key: str, val: int) -> None:
        self.node[key] = val

    def sum(self, prefix: str) -> int:
        return sum(val for key, val in self.node.items() if key.startswith(prefix))

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)