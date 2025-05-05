#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            # Check if the elements are not of type int or float
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
                result.append(0)
            else:
                # Perform division if types are correct
                result.append(a / b)
        except ZeroDivisionError:
            # Handle division by zero error
            print("division by 0")
            result.append(0)
        except IndexError:
            # Handle cases where the lists are shorter than list_length
            print("out of range")
            result.append(0)
    return result
