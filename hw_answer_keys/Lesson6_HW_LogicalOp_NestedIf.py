def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40  # boolean expression: equals True or False
    else:
        return 40 <= cigars and cigars <= 60  # boolean expression: equals True or False


def caught_speeding(speed, is_birthday):
    # If it is your birthday, subtract 5 from the speed to give a leeway of 5
    if is_birthday:
        speed -= 5

    # Check which value to return
    if speed <= 60:
        return 0
    elif 60 < speed and speed <= 80:
        return 1
    else:
        return 2


#########################################################

# For Testing purposes
print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))

print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))

#########################################################

# Comprehension Questions
# a. T
# b. F
# c. F
# d. T
