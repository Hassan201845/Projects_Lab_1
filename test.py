def ReLu(number):
    # if number is positive, return number, return number
    #else, return 0
    if number > 0:
        return number
    else:
        return 0
print(ReLu(10))
print(ReLu(-1))
