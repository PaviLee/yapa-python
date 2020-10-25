# Question 1

num_of_numbers = int(input("How many numbers would you like to enter? "))
max_value = None

if num_of_numbers >= 1:
    max_value = int(input("Enter a number: "))

for i in range(num_of_numbers - 1):
    num = int(input("Enter a number: "))
    if num > max_value:
        max_value = num

print("Largest number: " + str(max_value))

#########################################################

# Question 2

count_of_even_nums = 0

for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        count_of_even_nums += 1

print("Number of even numbers: " + str(count_of_even_nums))

#########################################################

# Question 3

num = int(input("Enter a number: "))

for i in range(1, num * num + 1):
    if i % num == 0:
        print(i)
