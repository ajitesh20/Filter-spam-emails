import math
# for murmurhash
import mmh3
# for representing bit array
from bitarray import bitarray

# defining bloom filter class
class BloomFilter(object):
    '''
    Implementation of bloom filter
    '''
    def __init__(self, item_count, size):
        '''
        initialize the BloomFilter object
        '''
        self.item_count = item_count
        self.size = size
        self.hash_count = self.get_hash_count(item_count, size)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, item):
        '''
        Adds an item to the bloom filter
        :param item: the item to be added
        :return: none
        '''
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = True

    def check(self, item):
        '''
        Checks whether an item is present in the bloom filter or not
        :param item: the item to be checked
        :return: True or False
        '''
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if not self.bit_array[digest]:
                return False
        return True

    def get_hash_count(self, n, m):
        '''
        Returns the number of Hash functions to use
        :param n: the number of items in the list to be added to bloom filter
        :param m: number of bits in the bit array
        :return: Int
        '''

        # using formula k = m/n * ln(2)
        return math.ceil((m / n) * math.log(2))
