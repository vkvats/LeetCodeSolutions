class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_key = set()
        self.key_values = []

    def get(self, key: int) -> int:
        if key in self.cache_key:
            for k, v in self.key_values:
                if key == k:
                    value = v
                    # remove key,value and then insert on top
                    self.key_values.remove([key, value])
                    self.key_values.append([key, value])
                    return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache_key:
            if len(self.cache_key) == self.capacity:
                # remove key, value at index 0
                key_r, val_r = self.key_values.pop(0)
                self.cache_key.remove(key_r)
                # add new key,value
                self.cache_key.add(key)
                self.key_values.append([key, value])
            else:
                # add key,value
                self.cache_key.add(key)
                self.key_values.append([key, value])
        else:
            for k, v in self.key_values:
                if k == key:
                    self.key_values.remove([key, v])
                    self.key_values.append([key, value])

# Solution from leetcode (using Ordered dict)
class LRUCache(object):
    def __init__(self, capacity):
        self.size = capacity
        self.mapping = OrderedDict()

    def get(self, key):
        if key in self.mapping:
           result =  self.mapping[key]
           del self.mapping[key]
           self.mapping[key] = result
           return result
        else:
            return -1
    def put(self, key, value):
        insert = False
        if key in self.mapping:
        # Update case; delete first and insert ad the end
           del self.mapping[key]
           self.mapping[key] = value
        else:
            self.mapping[key] = value
            insert = True

        if insert and len(self.mapping) > self.size:
            self.mapping.popitem(last=False)