import logging
import math

logging.basicConfig(level=logging.INFO)

data_array = ['tom', 'dick', 'harry', 'jane', 'jeff', 'aura', 'ham', 'angelina',
              'clarence', 'judy', 'rodriguez']
bloom_filter_size = 64
fp_limit = .1


def get_limit():
    return fp_limit * float(100)


def hash1(name):
    result = (get_added_chars_in_string(name) * 107) % bloom_filter_size
    logging.debug("Hash 1 {}".format(str(result)))
    return result


def hash2(name):
    result = (get_added_chars_in_string(name) * 37) % bloom_filter_size
    logging.debug("Hash 2 {}".format(str(result)))
    return result


def hash3(name):
    result = (get_added_chars_in_string(name) * 257) % bloom_filter_size
    logging.debug("Hash 3 {}".format(str(result)))
    return result


def get_added_chars_in_string(name):
    sum = 0
    for element in name:
        sum += ord(element)
    return sum


def set_bloom_bit(bloom_filter, bit_location):
    return bloom_filter | 1 << bit_location


def check_bloom_filter_bit(bloom_filter, bit_location):
    bit_location_index = bit_location
    logging.debug("Bit location {}".format(bit_location_index))
    logging.debug("Filter {}".format(get_bloom_filter_array(bloom_filter)))
    logging.debug("pos    {}\n".format(get_bit_number(bloom_filter)))

    logging.debug("mask  {}".format(get_bloom_filter_array(1 << bit_location_index)))
    logging.debug("pos   {}\n".format(get_bit_number(1 << bit_location_index)))

    logging.debug("result  {}".format(get_bloom_filter_array(bloom_filter & (1 << bit_location_index))))
    logging.debug("pos     {}\n".format(get_bit_number(bloom_filter & (1 << bit_location_index))))
    if bloom_filter & (1 << bit_location_index):
        logging.debug("True")
        return True
    logging.debug("False")
    return False


def build_bloom_filter(data_set):
    bloom_filter = 0
    for name in data_set:
        bloom_filter = add_name_to_bloom_filter(bloom_filter, name)
    logging.debug("The data set {}".format(data_set))
    logging.debug("Has the following Bloom Filter {}".format(bin(bloom_filter)))
    get_fp_rate()
    return bloom_filter


def add_name_to_bloom_filter(bloom_filter, name):
    name_hash_keys = hashes_name(name)
    bloom_filter = add_hash_to_filter(bloom_filter, name_hash_keys)
    return bloom_filter


def add_hash_to_filter(bloom_filter, name_hash_set):
    for name_hash in name_hash_set:
        bloom_filter = set_bloom_bit(bloom_filter, name_hash)
    return bloom_filter


def check_name_in_bloom_filter(bloom_filter, name):
    name_hash_set = hashes_name(name)
    logging.debug("hashes is {}".format(name_hash_set))
    for current_hash in name_hash_set:
        return check_bloom_filter_bit(bloom_filter, current_hash)


def get_bloom_filter_array(bloom_filter):
    bit_array = []
    bits = str(bin(bloom_filter))
    for char in bits:
        bit_array.append(' ' + char)
    return bit_array


def get_bit_number(bloom_filter):
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


# TODO: calculate hash collisions
def hashes_name(name):
    hash_keys = list()
    hash_keys.append(hash1(name))
    hash_keys.append(hash2(name))
    hash_keys.append(hash3(name))
    logging.debug("Hash Keys for name {} are {}".format(name, hash_keys))
    return hash_keys


# ref https://en.wikipedia.org/wiki/Bloom_filter
def get_fp_rate():
    number_of_hashes = 3
    number_of_elements = len(data_array)
    power_base = 1 - math.exp(-(number_of_hashes * number_of_elements)/bloom_filter_size)
    fp_rate = math.pow(power_base, number_of_hashes)
    logging.debug("root is %{}".format(fp_rate * 100))
    return fp_rate
