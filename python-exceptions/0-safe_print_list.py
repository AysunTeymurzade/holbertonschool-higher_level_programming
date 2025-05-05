#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')  # Print elements without a newline after each
            count += 1
    except IndexError:
        pass  # If there is an IndexError, just stop printing

    print()  # Print a newline at the end
    return count
