#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create an empty list to store the result
    result = []
    # Iterate through the elements of the input list
    for num in my_list:
        # Append True if the number is divisible by 2, otherwise False
        result.append(num % 2 == 0)
    # Return the result list
    return result
