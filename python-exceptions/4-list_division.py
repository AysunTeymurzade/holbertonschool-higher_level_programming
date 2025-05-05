#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Ensure that the current indices are within the range of both lists
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            # Ensure that both elements are either integers or floats
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")

            # Perform the division
            result.append(my_list_1[i] / my_list_2[i])

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            # This block is executed regardless of whether an exception was raised
            pass

    return result
