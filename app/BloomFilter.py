import logging
import math

logging.basicConfig(level=logging.INFO)

data_array = ['tom', 'dick', 'harry', 'jane', 'jeff', 'aura', 'ham', 'angelina',
              'clarence', 'judy', 'rodriguez', 'torres']
bloom_filter_size = 64
fp_limit = .1


def getlimit():
    return fp_limit * float(100)


def hash1(name):
    result = (getaddedcharsinstring(name) * 107) % bloom_filter_size
    logging.debug("Hash 1 {}".format(str(result)))
    return result


def hash2(name):
    result = (getaddedcharsinstring(name) * 37) % bloom_filter_size
    logging.debug("Hash 2 {}".format(str(result)))
    return result


def hash3(name):
    result = (getaddedcharsinstring(name) * 257) % bloom_filter_size
    logging.debug("Hash 3 {}".format(str(result)))
    return result


def getaddedcharsinstring(name):
    sum = 0
    for element in name:
        sum += ord(element)
    return sum


def setbloombit(bloom_filter, bit_location):
    return bloom_filter | 1 << bit_location


def checkbloomfilterbit(bloom_filter, bit_location):
    if bloom_filter & (1 << bit_location):
        return True
    return False


def buildbloomfilter(data_set):
    bloom_filter = 0
    for name in data_set:
        bloom_filter = addnametobloomfilter(bloom_filter, name)
    logging.debug("The data set {}".format(data_set))
    logging.debug("Has the following Bloom Filter {}".format(bin(bloom_filter)))
    getfprate()
    return bloom_filter


def addnametobloomfilter(bloom_filter, name):
    name_hash_keys = hashesname(name)
    bloom_filter = addhashtofilter(bloom_filter, name_hash_keys)
    return bloom_filter


def addhashtofilter(bloom_filter, name_hash_set):
    for hash in name_hash_set:
        bloom_filter = setbloombit(bloom_filter, hash)
    return bloom_filter


def checknameinbloomfilter(bloom_filter, name):
    name_hash_set = hashesname(name)
    for hash in name_hash_set:
        if(checkbloomfilterbit(bloom_filter, hash)):
            return True
    return False


def hashesname(name):
    hash_keys = []
    hash_keys.append(hash1(name))
    hash_keys.append(hash2(name))
    hash_keys.append(hash3(name))
    logging.debug("Hash Keys for name {} are {}".format(name, hash_keys))
    return hash_keys

# ref https://en.wikipedia.org/wiki/Bloom_filter
def getfprate():
    number_of_hashes = 3
    number_of_elements = len(data_array)
    power_base = 1 - math.exp(-(number_of_hashes * number_of_elements)/bloom_filter_size)
    fp_rate = math.pow(power_base, number_of_hashes)
    logging.debug("root is %{}".format(fp_rate * 100))
    return fp_rate
