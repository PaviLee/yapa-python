# Question 1

def sum67(nums):
    sum = 0
    inInterval67 = False

    for i in nums:
        if i == 6:
            inInterval67 = True
        elif not inInterval67:
            sum = sum + i
        elif i == 7:
            inInterval67 = False

    return sum


#########################################################

# Question 2

def has22(nums):
    hasTwoBefore = False

    for i in nums:
        if hasTwoBefore:
            if i == 2:
                return True
            else:
                hasTwoBefore = False
        elif i == 2:
            hasTwoBefore = True

    return False
