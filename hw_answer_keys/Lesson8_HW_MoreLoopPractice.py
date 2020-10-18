# Question 1

number = 1

while not((number ** 3) % 1000 == 888):
    number += 1

print("The number is " + str(number) + ".")

#########################################################

# Question 2

num_of_terms = int(input("How many numbers from the Fibonacci sequence do you want? "))

print("Fibonacci sequence:")

first = 1  # Current term is first
second = 1

while num_of_terms > 0:
    print(first)

    # Sets first to the second
    # Sets second to previous first + itself
    temp = first
    first = second
    second += temp

    num_of_terms -= 1
