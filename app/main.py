from BloomFilter import *

print('welcome to Bloom filter arrays')

print('The test array is: ')
print(data_array)

print('The bloom filter size is: ' + str(bloom_filter_size))

# bloom_filter_size = input("what size bloom filter do you want? ")
#
# hash_number = input("How many hash's do you want to use? (1-3) ")

bloom_filter = buildbloomfilter(data_array)

print('The Bloom filter is: ' + bin(bloom_filter))

while True:
    try:
        new_name = input('What would you like to add to the data set? ')
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    is_in_set = checknameinbloomfilter(bloom_filter, new_name)

    if is_in_set:
        print('Sorry the name exists. Please choose a different name')
    else:
        print('Name is not in set. You can use it')
        bloom_filter = addnametobloomfilter(bloom_filter, new_name)
        data_array.append(new_name)
        print('The new data set is array is: ')
        print(data_array)
        print('The new Bloom Filter is: ' + bin(bloom_filter))


    try_again = input('Would you like to try another name(Y/N)? ')

    if try_again in ('y', 'Y'):
        continue
    else:
        break
