my_list = []
for number in range ( 1, 51, 5 ) :
    my_list.append ( number )
print ( my_list )


def get_length_of_list_without_using_length_function ( a_list ) :
    num = 0
    for item in a_list:
        num += 1
    return num


def sum_of_items_in_even_positions_of_list_function(mylist) :
    even_sum = 0
    for item in my_list [ 0 : get_length_of_list_without_using_length_function ( my_list ) - 1 : 2 ] :
        even_sum += item
    return even_sum


def sum_of_items_in_odd_positions_of_list_function ( mylist ) :
    odd_sum = 0
    for item in my_list [ 1 :get_length_of_list_without_using_length_function ( my_list ) - 1 : 2 ] :
        odd_sum += item
    return odd_sum


def function_get_average_of_number_in_list_function ( a_list ) :
    sum_of_numbers_in_list = 0
    average = 0
    for item in a_list :
        sum_of_numbers_in_list += item
        average = sum_of_numbers_in_list / get_length_of_list_without_using_length_function ( a_list )
    return average


def get_the_largest_element_in_list_function ( a_list ) :
    largest = a_list [ 0 ]
    for item in a_list :
        if item > largest :
            largest = item
    return largest


def get_the_smallest_element_in_list_function ( a_list ) :
    smallest = a_list [ 0 ]
    for item in a_list :
        if item < smallest :
            smallest = item
    return smallest


def count_the_number_of_strings_in_list_function ( a_list ) :
    string_list = str ( a_list )
    count_of_strings = 0
    for item in string_list :
        count_of_strings += 1
    if count_of_strings >= 2 and (string_list [ 0 ] == string_list [ count_of_strings - 1 ]) :
        return string_list


print ( count_the_number_of_strings_in_list_function ( my_list ) )
print ( get_the_smallest_element_in_list_function ( my_list ) )
print ( function_get_average_of_number_in_list_function ( my_list ) )
print ( get_the_largest_element_in_list_function ( my_list ) )
print ( get_length_of_list_without_using_length_function ( my_list ) )
print ( sum_of_items_in_odd_positions_of_list_function ( my_list ) )
print ( sum_of_items_in_odd_positions_of_list_function ( my_list ) )
