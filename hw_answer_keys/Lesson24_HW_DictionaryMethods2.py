def remove_key(dictonary, key):
    dictonary.pop(key)


def remove_duplicates(dictionary):
    temp = {}

    for key, value in dictionary.items():
        if value not in temp.values():
            temp[key] = value

    return temp


def is_empty(dictionary):
    return not bool(dictionary)


data = {
    "Anna": 76,
    "Bob": 60,
    "Carol": 60,
    "David": 99,
    "Eric": 99,
    "Finn": 100
}

print(data)
remove_key(data, "Finn")
print(data)

print(remove_duplicates(data))

print(is_empty({}))
print(is_empty(data))
