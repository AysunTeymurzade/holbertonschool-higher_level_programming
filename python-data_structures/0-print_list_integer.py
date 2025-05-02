#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if not isinstance(i, int):
            raise TypeError("list must contain only integers")
        print("{:d}".format(i))
