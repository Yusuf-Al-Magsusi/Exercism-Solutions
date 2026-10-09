def is_armstrong_number(number):
    sum = 0
    s = str(number)
    length = len(s)
    for ch in s:
        sum += int(ch)**length
    if sum == number:
        return True
    return False 