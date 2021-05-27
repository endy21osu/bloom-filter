import logging
import math
from random import choice
from string import ascii_uppercase

logging.basicConfig(level=logging.INFO)


def get_added_chars_in_string(name):
    char_sum = 0
    for element in name:
        char_sum += ord(element)
    return char_sum


def print_bloom_filter_bit_array(bloom_filter):
    bit_array = []
    bits = str(bin(bloom_filter))
    for char in bits:
        bit_array.append(' ' + char)
    return bit_array


def print_bit_position(bloom_filter):
    bit_numbers = []
    bits = str(bin(bloom_filter))
    count = len(bits)
    while count > 0:
        if count < 10:
            bit_str = '0' + str(count)
        else:
            bit_str = str(count)
        bit_numbers.append(bit_str)
        count -= 1
    return bit_numbers


def check_bloom_filter_bit(bloom_filter, bit_location):
    bit_location_index = bit_location
    mask = 1 << bit_location_index
    logging.debug("**check_bloom_filter_bit**")
    is_in_filter = bloom_filter & mask
    logging.debug("Bit location {}".format(bit_location_index))
    logging.debug("Filter {}".format(print_bloom_filter_bit_array(bloom_filter)))
    logging.debug("pos    {}\n".format(print_bit_position(bloom_filter)))

    logging.debug("mask  {}".format(print_bloom_filter_bit_array(mask)))
    logging.debug("pos   {}\n".format(print_bit_position(mask)))

    logging.debug("result  {}".format(print_bloom_filter_bit_array(is_in_filter)))
    logging.debug("pos     {}\n".format(print_bit_position(is_in_filter)))
    if is_in_filter:
        logging.debug("True")
        return True
    logging.debug("False")
    return False


def set_bloom_bit(bloom_filter, bit_location):
    bit_location_index = bit_location
    mask = 1 << bit_location_index
    logging.debug("**set_bloom_bit**")
    logging.debug("Bit location {}".format(bit_location_index))
    logging.debug("Filter {}".format(print_bloom_filter_bit_array(bloom_filter)))
    logging.debug("pos    {}\n".format(print_bit_position(bloom_filter)))

    updated_bloom_filter = bloom_filter | mask

    logging.debug("mask  {}".format(print_bloom_filter_bit_array(mask)))
    logging.debug("pos   {}\n".format(print_bit_position(mask)))

    logging.debug("result  {}".format(print_bloom_filter_bit_array(updated_bloom_filter)))
    logging.debug("pos     {}\n".format(print_bit_position(updated_bloom_filter)))
    return updated_bloom_filter


def add_hash_to_filter(bloom_filter, name_hash_set):
    for name_hash in name_hash_set:
        bloom_filter = set_bloom_bit(bloom_filter, name_hash)
    return bloom_filter


class BloomFilter:
    large_strings_array = list()
    bloom_filter_bit_array = 0
    fp_limit = 0
    size = 64

    def __init__(self, size):
        self.size = size
        self.create_random_array()
        self.fp_limit = .1

    def create_random_array(self):
        for counter in range(0, 100):
            self.large_strings_array.append(''.join(choice(ascii_uppercase) for i in range(12)))
        logging.debug("large array  {}".format(self.large_strings_array))

    def add_to_array(self, new_name):
        self.large_strings_array.append(new_name)

    # TODO: add this into an organized class
    def get_limit(self):
        return self.fp_limit * float(100)

    def set_size(self, size):
        self.size = size

    def hash1(self, name):
        logging.debug("filter size  {}".format(self.size))
        result = (get_added_chars_in_string(name) * 107) % int(self.size)
        logging.debug("Hash 1 {}".format(str(result)))
        return result

    def hash2(self, name):
        logging.debug("filter size  {}".format(self.size))
        result = (get_added_chars_in_string(name) * 37) % int(self.size)
        logging.debug("Hash 2 {}".format(str(result)))
        return result

    def hash3(self, name):
        logging.debug("filter size  {}".format(self.size))
        result = (get_added_chars_in_string(name) * 257) % int(self.size)
        logging.debug("Hash 3 {}".format(str(result)))
        return result

    def build_bloom_filter(self, data_set):
        for name in data_set:
            self.bloom_filter_bit_array = self.add_name_to_bloom_filter(int(self.bloom_filter_bit_array), name)
        logging.debug("The data set {}".format(data_set))
        logging.debug("Has the following Bloom Filter {}".format(bin(self.bloom_filter_bit_array)))
        self.get_fp_rate(self.size)
        return self.bloom_filter_bit_array

    def add_name_to_bloom_filter(self, bloom_filter, name):
        name_hash_keys = self.hashes_name(name)
        self.bloom_filter_bit_array = add_hash_to_filter(bloom_filter, name_hash_keys)
        return self.bloom_filter_bit_array

    def check_name_in_bloom_filter(self, bloom_filter, name):
        name_hash_set = self.hashes_name(name)
        logging.debug("hashes is {}".format(name_hash_set))
        is_in_filter = False
        for current_hash in name_hash_set:
            is_in_filter = is_in_filter | check_bloom_filter_bit(bloom_filter, current_hash)
            if is_in_filter:
                break
        return is_in_filter

    # TODO: calculate hash collisions
    def hashes_name(self, name):
        hash_keys = list()
        hash_keys.append(self.hash1(name))
        hash_keys.append(self.hash2(name))
        hash_keys.append(self.hash3(name))
        logging.debug("Hash Keys for name {} are {}".format(name, hash_keys))
        return hash_keys

    # TODO: check bloom
    # ref https://en.wikipedia.org/wiki/Bloom_filter
    def get_fp_rate(self, size):
        number_of_hashes = 3
        number_of_elements = len(self.large_strings_array)
        logging.debug("number_of_elements {} ".format(number_of_elements))
        logging.debug("size {} ".format(size))
        power_base = 1 - math.exp((-number_of_hashes * number_of_elements) / int(size))
        logging.debug("power_base {} ".format(power_base))
        fp_rate = math.pow(power_base, number_of_hashes)
        logging.debug("rate is %{}".format(fp_rate * 100))
        return fp_rate
