class HashTable(object):
    def __init__(self):
        self.size = 11
        self.data = [None] * self.size
        self.key = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)
        if self.key[hash_value] is None:
            self.key[hash_value] = key
            self.data[hash_value] = value
        else:
            next_hash = self.rehash(hash_value)
            while self.key[next_hash] != key and self.key[next_hash] is not None:
                next_hash = self.rehash(next_hash)
            self.key[next_hash] = key
            self.data[next_hash] = value

    def get(self, key):
        hash_value = self.hash_function(key)
        while self.key[hash_value] == key and self.key[hash_value] is not None:
            if self.key[hash_value] == key:
                return self.data[hash_value]
            else:
                position = self.rehash(hash_value)
                if position == hash_value:
                    return None

    def __getitem__(self, key):
        return self.get[key]

    def __setitem__(self, key, value):
        self.put(key, value)















