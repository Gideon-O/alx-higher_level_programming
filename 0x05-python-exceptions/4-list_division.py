#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Function that divides between two list elements
    Operates by dividing between two elements of the same index
    Returns a new list of lenght 'list_length'
    """
    new_list = []
    result = 0
    for i in range(list_lenght):
        try:
            result = my_list_1[i] / my_list_2
        except TypeError:
            print("Wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
