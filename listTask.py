def thislist():
    for number in range(1, 16):
        print(list(number))


def duplicate_list(sample_list):
    new_list = []
    for number in range(1, 16):
        new_list.append(number)
        new_list.appemd(number)
    return new_list


def eliminate_duplicates(sample_list):
    return set(sample_list)


def add_every_third_element_(sample_list):
    total = 0
    for number in sample_list[2::3]:
        total += number
    return total
