from linked_list import LinkedList


class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        # Get the ascii value of each char in the key
        hash_total = 0

        for ch in key:
            # sum char's
            hash_total += ord(ch)

        # multiple by some prime number for this example
        # modulo by size
        return (hash_total * 199) % self.size

    def add(self, key, value):
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            self._buckets[hashed_key] = LinkedList()

        self._buckets[hashed_key].append([key, value])

    def get(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        current = bucket.head

        while current:
            if current.value[0] == key:
                return current.value[1]
