import unittest

from BloomFilter import *

class TestHashOne(unittest.TestCase):
    def setUp(self) -> None:
        self.name = 'pete'
        self.filter = 0
        self.hashed_name = [58, 38, 46]
        self.data_array = ['tom', 'dick', 'harry', 'jane', 'pete']

    def tearDown(self) -> None:
        del self.name
        del self.filter
        del self.hashed_name
        del self.data_array

    def test_hash1(self):
        hash = hash1(self.name)
        self.assertEqual(True, hash == 58)

    def test_hash2(self):
        hash = hash2(self.name)
        self.assertEqual(True, hash == 38)

    def test_hash3(self):
        hash = hash3(self.name)
        self.assertEqual(True, hash == 46)

    def test_getAddedCharsInString(self):
        integer_rep = getaddedcharsinstring(self.name)
        self.assertEqual(True, integer_rep == 430)

    def test_hashesname(self):
        hashes_array = hashesname(self.name)
        self.assertEqual(True, len(hashes_array) == 3)

    def test_setbloombit(self):
        hash = hash1(self.name)
        self.filter = setbloombit(self.filter, hash)
        self.assertEqual(True, self.filter > 0)

    def test_checkbloomfilterbit(self):
        self.filter = setbloombit(self.filter, hash1(self.name))
        isSet = checkbloomfilterbit(self.filter, hash1(self.name))
        self.assertEqual(True, isSet)
        isSet = checkbloomfilterbit(self.filter, hash2(self.name))
        self.assertEqual(False, isSet)

    def test_buildbloomfilter(self):
        bloom_filter = buildbloomfilter(self.data_array)
        isSet = checkbloomfilterbit(bloom_filter, hash1(self.name))
        self.assertEqual(True, isSet)

    def test_addhashtofilter(self):
        bloom_filter = 0
        bloom_filter = addhashtofilter(bloom_filter, self.hashed_name)
        isSet = checknameinbloomfilter(bloom_filter, self.name)
        self.assertEqual(True, isSet)

    def test_addnametobloomfilter(self):
        bloom_filter = 0
        bloom_filter = addnametobloomfilter(bloom_filter, self.name)
        isSet = checknameinbloomfilter(bloom_filter, self.name)
        self.assertEqual(True, isSet)

    def test_checknameinbloomfilter(self):
        bloom_filter = 0
        bloom_filter = addhashtofilter(bloom_filter, self.hashed_name)
        isSet = checknameinbloomfilter(self.filter, self.name)
        self.assertEqual(False, isSet)

if __name__ == '__main__':
    unittest.main()
