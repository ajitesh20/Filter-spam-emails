import math
# for murmurhash
import mmh3
# for representing bucket set
from bitarray import bitarray


# defining bloom filter class
class BloomFilter(object):
    def __init__(self, item_count, size):
        self.item_count = item_count
        self.size = size
        self.hash_count = self.get_hash_count(item_count, size)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = True

    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if not self.bit_array[digest]:
                return False
        return True

    def get_hash_count(self, n, m):
        return math.ceil((m / n) * math.log(2))
