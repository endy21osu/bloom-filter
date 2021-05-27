import unittest

from BloomFilter import *

class TestHashOne(unittest.TestCase):
    def setUp(self) -> None:
        self.name = 'pete'

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
        integer_rep = getAddedCharsInString(self.name)
        self.assertEqual(True, integer_rep == 430)

    def test_hashsName(self):
        hashs_array = hashsName(self.name)
        self.assertEqual(True, len(hashs_array) == 3)


if __name__ == '__main__':
    unittest.main()
