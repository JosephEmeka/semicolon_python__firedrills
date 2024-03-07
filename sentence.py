sentence = "the palace is few miles away from the village but going to the palace to see startups is cool and fun"
new_sentence = sentence.split(" ")
new_dictionary = {}
for word in new_sentence:
    if word in new_dictionary:
        new_dictionary[word] += 1
    else:
        new_dictionary[word] = 1

test_input = "hello world! 123"


def check_number_of_alphabet(new_input):
    number_of_alpha = 0
    number_of_numbers = 0
    for items in new_input:
        if items.isalpha():
            number_of_alpha += 1
        if items.isdigit():
            number_of_numbers += 1
    return f"LETTERS {number_of_alpha} DIGITS {number_of_numbers}"


print(check_number_of_alphabet(test_input))

sentence = "Hello World"


def check_cases_in_sentence(sample_sentence):
    number_of_upper = 0
    number_of_lower = 0
    for item in sample_sentence:
        if item.isupper():
            number_of_upper += 1
        if item.islower():
            number_of_lower += 1
    return f'UPPER CASE {number_of_upper} LOWER CASE {number_of_lower}'


print(check_cases_in_sentence(sentence))
