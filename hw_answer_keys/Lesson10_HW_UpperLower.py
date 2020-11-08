# Question 1
word = input("What is your word? ")

if word.islower():
    print(word.upper())
elif word.isupper():
    print(word.lower() + word.lower())
else:
    print(word.upper() + word.lower())
