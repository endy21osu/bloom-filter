data_array = ['tom', 'dick', 'harry', 'jane']
bloom_filter_size = 64

def hash1(name):
    result = (getaddedcharsinstring(name) * 107) % bloom_filter_size
    print('Hash1 ' + str(result))
    return result


def hash2(name):
    result = (getaddedcharsinstring(name) * 37) % bloom_filter_size
    print('Hash2 ' + str(result))
    return result


def hash3(name):
    result = (getaddedcharsinstring(name) * 257) % bloom_filter_size
    print('Hash3 ' + str(result))
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
        name_hash_keys = hashesname(name)
        bloom_filter = addnametofilter(bloom_filter, name_hash_keys)
    return bloom_filter


def addnametofilter(bloom_filter, name_hash_set):
    for hash in name_hash_set:
        bloom_filter = setbloombit(bloom_filter, hash)
    return bloom_filter


def checknameinbloomfilter(bloom_filter, name_hash_set):
    for hash in name_hash_set:
        if(checkbloomfilterbit(bloom_filter, hash)):
            return True
    return False


def hashesname(name):
    hash_keys = []
    hash_keys.append(hash1(name))
    hash_keys.append(hash2(name))
    hash_keys.append(hash3(name))
    print(hash_keys)
    return hash_keys


# hashsName(input("what name do you want to check the bloom filter? "))
