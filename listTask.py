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
       for number in my_list[(middle_index-1): (middle_index+1)]:
           middle_sum += number
       middle_number = middle_sum / 2
    total = my_list[0] + my_list[-1] + middle_number
    return total
