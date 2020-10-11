# Question 1

counter = 2
while counter <= 20:
    if counter % 2 == 0:
        print(counter)
    counter += 1

#########################################################

# Question 2

lower_bound = int(input("What is the lower bound? "))
upper_bound = int(input("What is the upper bound? "))

while lower_bound <= upper_bound:
    if lower_bound % 2 == 1:
        print(lower_bound)
    lower_bound += 1
