import unittest
from BloomFilter import *

class TestHashOne(unittest.TestCase):
    def setUp(self) -> None:
        self.bloom_filter = BloomFilter(256)
        self.name = 'pete'
        self.filter = 0
        self.hashed_name = [58, 38, 46]
        # self.hashed_name = [26, 6, 14]
        self.data_array = ['tom', 'dick', 'harry', 'jane', 'pete']

    def tearDown(self) -> None:
        del self.name
        del self.bloom_filter
        del self.filter
        del self.hashed_name
        del self.data_array

    def test_hash1(self):
        hash = self.bloom_filter.hash1(self.name)
        self.assertEqual(True, hash == 186)

    def test_hash2(self):
        hash = self.bloom_filter.hash2(self.name)
        self.assertEqual(True, hash == 38)

    def test_hash3(self):
        hash = self.bloom_filter.hash3(self.name)
        self.assertEqual(True, hash == 174)

    def test_get_added_chars_in_string(self):
        integer_rep = get_added_chars_in_string(self.name)
        self.assertEqual(True, integer_rep == 430)

    def test_hashes_name(self):
        hashes_array = self.bloom_filter.hashes_name(self.name)
        self.assertEqual(True, len(hashes_array) == 3)

    def test_set_bloom_bit(self):
        hash = self.bloom_filter.hash1(self.name)
        self.filter = set_bloom_bit(self.filter, hash)
        self.assertEqual(True, self.filter > 0)

    def test_check_bloom_filter_bit(self):
        self.filter = set_bloom_bit(self.filter, self.bloom_filter.hash1(self.name))
        isSet = check_bloom_filter_bit(self.filter, self.bloom_filter.hash1(self.name))
        self.assertEqual(True, isSet)
        isSet = check_bloom_filter_bit(self.filter, self.bloom_filter.hash2(self.name))
        self.assertEqual(False, isSet)

    def test_build_bloom_filter(self):
        bloom_filter = self.bloom_filter.build_bloom_filter(self.data_array)
        isSet = check_bloom_filter_bit(bloom_filter, self.bloom_filter.hash1(self.name))
        self.assertEqual(True, isSet)

    def test_add_hash_to_filter(self):
        bloom_filter = 0
        bloom_filter = add_hash_to_filter(bloom_filter, self.hashed_name)
        is_set = self.bloom_filter.check_name_in_bloom_filter(bloom_filter, self.name)
        self.assertEqual(True, is_set)

    def test_add_name_to_bloom_filter(self):
        bloom_filter = 0
        bloom_filter = self.bloom_filter.add_name_to_bloom_filter(bloom_filter, self.name)
        is_set = self.bloom_filter.check_name_in_bloom_filter(bloom_filter, self.name)
        self.assertEqual(True, is_set)

    def test_check_name_in_bloom_filter(self):
        bloom_filter = 0
        add_hash_to_filter(bloom_filter, self.hashed_name)
        is_set = self.bloom_filter.check_name_in_bloom_filter(self.filter, self.name)
        self.assertEqual(False, is_set)

    def test_get_fp_rate(self):
        fp_rate = self.bloom_filter.get_fp_rate(64)
        self.assertEqual(False, fp_rate < self.bloom_filter.fp_limit)
        self.bloom_filter.get_fp_rate(4000)
        fp_rate = self.bloom_filter.get_fp_rate(8000)
        self.bloom_filter.get_fp_rate(16000)
        self.bloom_filter.get_fp_rate(320000)
        self.assertEqual(True, fp_rate < self.bloom_filter.fp_limit)

if __name__ == '__main__':
    unittest.main()
