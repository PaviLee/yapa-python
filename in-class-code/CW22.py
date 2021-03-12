# Key = Name
# Value = Age

# First way to make a dictionary object
database = {}
database["Frank"] = 21
database["Mary"] = 7
database["John"] = 10

print(database)

# Second way to make a dictionary object
database2 = {
    "Frank": 21,
    "Mary": 7,
    "Jill": 10
}

print(database2)

for name, age in database2.items():
    print(name + " is " + str(age) + " years old")

# Make a phonebook dictionary
# 3 key-value pairs
# Key = name of person
# Value = distinct phone number
