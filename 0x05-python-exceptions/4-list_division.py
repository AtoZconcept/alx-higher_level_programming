#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length

    try:
        for i in range(list_length):
            if i < len(my_list_1) and i < len(my_list_2):
                if (isinstance(my_list_1[i], (int, float))
                        and isinstance(my_list_2[i], (int, float))):
                    if my_list_2[i] == 0:
                        print('division by 0')
                    else:
                        result[i] = my_list_1[i] / my_list_2[i]
                else:
                    print('wrong type')
            else:
                print("out of range")
    except ZeroDivisionError:
        pass
    finally:
        return result
