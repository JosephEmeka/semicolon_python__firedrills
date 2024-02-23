sentence = "the palace is few miles away from the village but going to the palace to see startups is cool and fun"
new_sentence = sentence.split(" ")
new_dictionary = {}
for word in new_sentence:
    if word in new_dictionary:
        new_dictionary[word] += 1
    else:
        new_dictionary[word] = 1

print(new_dictionary)
