student_ids = {
    "Anna": 32434,
    "Bob": 54365,
    "Candice": 84573,
    "Dave": 56836,
    "Ernest": 74954,
    "Fred": 58657,
    "George": 96745
}

for key, value in student_ids.items():
    print(key + " has the student id of " + str(value))

student_ids.pop("George")
student_ids.pop("Dave")

student_ids["Gina"] = 45767
student_ids["Derek"] = 34343

for key, value in student_ids.items():
    print(key + " has the student id of " + str(value))
