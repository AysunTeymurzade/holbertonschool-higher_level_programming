#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):  # Check if the element is an integer
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break
    print()  # Print a new line after the printed integers
    return count
