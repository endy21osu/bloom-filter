from BloomFilter import *

print('welcome to Bloom filter arrays')

print('The test array is: ')
print(data_array)

print('The bloom filter size is: ' + str(bloom_filter_size))

# bloom_filter_size = input("what size bloom filter do you want? ")
#
# hash_number = input("How many hash's do you want to use? (1-3) ")

print('The False Positive rate limit is set to: %' + str(getlimit()))

bloom_filter = buildbloomfilter(data_array)

print('The Bloom filter is: ' + bin(bloom_filter))
print('The False Positive Rate  is: %' + str(getfprate()))
print('')
additions = 1

while True:

    print('Entry ' + str(additions))
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
    new_name = input('What would you like to add to the data set? ')
    is_in_set = checknameinbloomfilter(bloom_filter, new_name)

    if is_in_set:
        print('Sorry the name exists. Please choose a different name')
    else:
        print('Name is not in set. You can use it')
        bloom_filter = addnametobloomfilter(bloom_filter, new_name)
        data_array.append(new_name)
        print('The new data set is array is: ')
        print(data_array)
        additions += 1
        print('The New Bloom Filter is: ' + bin(bloom_filter))
        print('The New False Positive Rate  is: %' + str(getfprate()))

    if getfprate() > fp_limit:
        print('The False Positive Rate is too high. Please consider adding')
        print('a larger Bloom filter or more hash functions.')

    print('-----------------------------------------------------')
    print('')

    try_again = input('Would you like to try another name(Y/N)? ')

    if try_again in ('y', 'Y'):
        continue
    else:
        break
