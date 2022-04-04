def countdown(num):
    countdown_list = []
    for i in range(num, -1, -1):
        countdown_list.append(i)
    return countdown_list

# print(countdown(5))


def print_and_return(num_list):
    print(num_list[0])
    return num_list[1]

# print(print_and_return([1, 2]))


def first_plus_length(num_list):
    return int(num_list[0]) + len(num_list)


# print(first_plus_length([1, 2, 3, 4, 5]))

# def values_greater_than_second(num_list):
#     if len(num_list) < 2:
#         return False

#     new_list = []
#     for i in range(len(num_list)): # range(start, stop, increment)
#         if num_list[i] > num_list[1]: # if value is greater than the value of the second element
#             new_list.append(num_list[i]) # add to new list
#     print(len(new_list)) # prints the length of the new list
#     return new_list

def values_greater_than_second(num_list):
    if len(num_list) < 2:
        return False

    new_list = []
    for value in num_list:
        if value > num_list[1]:
            new_list.append(value)

    print(len(new_list))
    return new_list


# print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
# print(values_greater_than_second([3]))

def length_and_value(length, value):
    new_list = []
    for i in range(length):
        new_list.append(value)
    return new_list


# print(length_and_value(4, 7))
# print(length_and_value(6, 2))
