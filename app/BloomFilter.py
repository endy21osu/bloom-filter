print('welcome to Bloom filter arrays')

data_array = ['tom', 'dick', 'harry', 'jane']
bloom_filter_size = 128

# bloom_filter_size = input("what size bloom filter do you want? ")
#
# hash_number = input("How many hash's do you want to use? (1-3) ")

print("The Bloom filter size is " + str(bloom_filter_size))


def hash1(name):
    result = (getAddedCharsInString(name) * 107) % bloom_filter_size
    print('Hash1 ' + str(result))
    return result


def hash2(name):
    result = (getAddedCharsInString(name) * 37) % bloom_filter_size
    print('Hash2 ' + str(result))
    return result


def hash3(name):
    result = (getAddedCharsInString(name) * 257) % bloom_filter_size
    print('Hash3 ' + str(result))
    return result


def getAddedCharsInString(name):
    sum = 0
    for element in name:
        sum += ord(element)
    return sum


def hashsName(name):
    hash_keys = []
    hash_keys.append(hash1(name))
    hash_keys.append(hash2(name))
    hash_keys.append(hash3(name))
    print(hash_keys)
    return hash_keys


# hashsName(input("what name do you want to check the bloom filter? "))
