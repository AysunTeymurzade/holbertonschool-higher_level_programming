#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Loop through the list in reverse order
    for num in my_list[::-1]:
        print("{:d}".format(num))
