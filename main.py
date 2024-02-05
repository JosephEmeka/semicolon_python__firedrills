def arrange_list(my_list):
    sorted_list = set(my_list)
    my_new_sorted_list = list(sorted_list)
    return my_new_sorted_list


sampleList = [10, 2, 8, 9, 3, 4, 1, 5]

print(arrange_list(sampleList))


def arrange_list_in_ascending_order(my_list):
    for number in range(len(my_list)):
        for value in range(number + 1, len(my_list)):
            if my_list[number] > my_list[value]:
                my_list[number], my_list[value] = my_list[value], my_list[number]

    return my_list


my_new_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]

print(arrange_list_in_ascending_order(my_new_list))


def arrange_list_in_descending_order(my_list):
    for number in range(len(my_list)):
        for value in range(number + 1, len(my_list)):
            if my_list[number] < my_list[value]:
                my_list[number], my_list[value] = my_list[value], my_list[number]
    return my_list


print(arrange_list_in_descending_order(my_new_list))


def search_key(data: list, key: int) -> int:
    for index, value in enumerate(data):
        if value == key:
            return index
        return -1


print(search_key([10, 2, 8, 9, 3, 4, 1, 5], 5))
