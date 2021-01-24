def abs_value(num):
    '''
    Returns the absolute value of the input.

    :param num: inputted number
    :return: the absolute value of num
    '''

    # This was classwork

    if num < 0:
        num = num * -1

    return num


def find_min(num1, num2):
    '''
    Returns the smallest number of the two inputs.

    :param num1: first inputted number
    :param num2: second inputted number
    :return: the smallest number of the two inputs
    '''

    if num1 < num2:
        return num1
    else:
        return num2


def add_three_nums(num1, num2, num3):
    '''
    Returns the sum of the three inputs

    :param num1: first inputted number
    :param num2: second inputted number
    :param num3: third inputted number
    :return: the sum of the three inputs
    '''

    return num1 + num2 + num3


# Test functions here
print(abs_value(1))
print(abs_value(-1))
print(abs_value(-0.25))

print(find_min(10, 20))
print(find_min(-10, 20))
print(find_min(10, -20))

print(add_three_nums(1, 2, 3))
print(add_three_nums(-1, 2, -3))
print(add_three_nums(10, -30, 4))
