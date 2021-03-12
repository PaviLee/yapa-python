gradebook = {
    "Anna": 70,
    "Bob": 90,
    "Carl": 40,
    "David": 87,
    "David": 100
}

gradebook.pop("Bob")
gradebook.pop("Carl")
gradebook["Gina"] = 90
gradebook["Hugo"] = 10

print(gradebook)

# clear()
# gradebook.clear()
# print(gradebook)

# copy()
# gradebook_copy = gradebook.copy()
# print(gradebook_copy)

# fromkeys()
# keys = ("Anna", "Bob", "Carl")
# value = 100
# fromkeys_gradebook = dict.fromkeys(keys, value)
#
# print(fromkeys_gradebook)

# IMPORTANT - get()
# print(gradebook.get("Anna"))

# IMPORTANT - items() - Returns a list containing a tuple for each key value pair
# print(gradebook.items())

# IMPORTANT - keys()
# print(gradebook.keys())

# IMPORTANT - pop()
# gradebook.pop("Anna")
# print(gradebook)
