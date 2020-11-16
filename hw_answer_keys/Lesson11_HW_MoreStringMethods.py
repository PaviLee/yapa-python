# Question 1

text = input("Enter some text: ")
found_a = False
index = 1

for c in text:
    if c.lower() == 'a':
        found_a = True
        print(index)
    index += 1

if not found_a:
    print(0)

#########################################################

# Question 2

text = input("Enter some text: ")

for c in text:
    print(c + c)
