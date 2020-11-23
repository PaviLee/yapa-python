# Question 1

database = [2, 4, 1, 7, 7, 3, 8, 3, 7, 3]
truth_list = []

for num in database:
    truth_list.append(num % 2)

print("Truth List")
print(truth_list)
print(database[1])
print(truth_list[7])

#########################################################

# Question 2

original_list = []

original_list.append("there")
original_list.append("IS")
original_list.append("oNly")
original_list.append("onE")
original_list.append("Thing")
original_list.append("worst")

uppercase_list = []

for word in original_list:
    uppercase_list.append(word.upper())

lowercase_list = []

for word in original_list:
    lowercase_list.append(word.lower())

print("Original List")
print(original_list)

print("Uppercase List")
print(uppercase_list)

print("Lowercase List")
print(lowercase_list)
