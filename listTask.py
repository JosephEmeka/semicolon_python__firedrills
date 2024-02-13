def this_list():
    new_list = []
    for number in range(1, 16):
        new_list.append(number)
    return new_list


def duplicate_list(sample_list):
    new_list = []
    my_duplicate_list = []
    for number in range(1, 16):
        new_list.append(number)
        my_duplicate_list = new_list + new_list
    return my_duplicate_list


def eliminate_duplicates(sample_list):
    new_list = []
    set_of_numbers = set(sample_list)
    for number in set_of_numbers:
        new_list.append(number)
    return new_list


def add_every_third_element(sample_list):
    total = 0
    for number in sample_list[2::3]:
        total += number
    return total


def sum_first_middle_and_last_element(my_list):
    total = 0
    middle_sum = 0
    middle_index = len(my_list) // 2
    if len(my_list) % 2 == 0:
        for number in my_list[(middle_index - 1): (middle_index + 1)]:
            middle_sum += number
        middle_number = middle_sum / 2
    total = my_list[0] + my_list[-1] + middle_number
    return total


def sum_collection(my_set):
    sum_element = 0
    for element in my_set:
        sum_element += element
    return sum_element


def remove_item(my_sample_set, my_sample_number):
    if my_sample_number in my_sample_set:
        my_sample_set.remove(my_sample_number)
        return my_sample_number
    else:
        return None


def find_intersection(my_first_set, my_second_set):
    intersection_set = set()
    for element in my_first_set:
        if element in my_second_set:
            intersection_set.add(element)
    return intersection_set

    for numbers in range[1:11]:
        user_input = input(int("Enter a number: "))
        new_set = set()
        new_set.add(user_input)
        print(new_set)


def find_intersection_set(my_first_string, my_second_string):
    new_string = my_second_string[0:2] + my_first_string[2:] + " " + my_first_string[0:2] + my_second_string[2:]
    return new_string
