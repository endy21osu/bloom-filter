from BloomFilter import *
import textwrap

def print_pretty(output_string):
    print(textwrap.fill(str(output_string), 300))


print_pretty('welcome to Bloom filter arrays')

bloom_filter_size = input("what size bloom filter do you want? ")

bloom_filter = BloomFilter(bloom_filter_size)

print_pretty('The new bloom filter size is: ' + str(bloom_filter.size))
#
# hash_number = input("How many hash's do you want to use? (1-3) ")

print_pretty('The False Positive rate limit is set to: %' + str(bloom_filter.get_limit()))

bloom_filter.build_bloom_filter(bloom_filter.large_strings_array)

print_pretty('The test array is: ')
print_pretty(bloom_filter.large_strings_array)

print_pretty('The Bloom filter is: ' + bin(bloom_filter.bloom_filter_bit_array))
print_pretty('The False Positive Rate  is: %' + str(bloom_filter.get_fp_rate(float(bloom_filter.size))))
print_pretty('')
additions = 1

while True:

    print_pretty('Entry ' + str(additions))
    print_pretty('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
    new_name = input('What would you like to add to the data set? ')
    is_in_set = bloom_filter.check_name_in_bloom_filter(bloom_filter.bloom_filter_bit_array, new_name)

    if is_in_set:
        print_pretty('Sorry the name exists. Please choose a different name')
    else:
        print_pretty('Name is not in set. You can use it')
        bloom_filter.add_name_to_bloom_filter(bloom_filter.bloom_filter_bit_array, new_name)
        bloom_filter.add_to_array(new_name)
        print_pretty('The new data set is array is: ')
        print_pretty(bloom_filter.large_strings_array)
        additions += 1
        print_pretty('The New Bloom Filter is: ' + bin(bloom_filter.bloom_filter_bit_array))
        print_pretty('The New False Positive Rate  is: %' + str(bloom_filter.get_fp_rate(bloom_filter.size)))

    if bloom_filter.get_fp_rate(bloom_filter.size) > bloom_filter.fp_limit:
        print_pretty('The False Positive Rate is too high. Please consider adding')
        print_pretty('a larger Bloom filter or more hash functions.')

    print_pretty('-----------------------------------------------------')
    print_pretty('')

    try_again = input('Would you like to try another name(Y/N)? ')

    if try_again in ('y', 'Y'):
        continue
    else:
        break


