# Question 1

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


#########################################################

# Question 2

def sum13(nums):
    sum = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i = i + 2
        else:
            sum = sum + nums[i]
            i = i + 1

    return sum
