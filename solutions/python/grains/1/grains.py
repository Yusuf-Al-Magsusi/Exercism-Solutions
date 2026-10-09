def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    elif number == 1:
        return 1
    grain = 1
    for i in range(number-1):
        grain *= 2
    return grain

def total():
    grain = 1
    for i in range(64):
        grain *= 2
    return grain-1
        
