def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        
    steps = 0
    current_number = number

    while current_number != 1:
        if current_number % 2 == 0:
            current_number /= 2
            steps += 1
        else:
            current_number *= 3
            current_number += 1
            steps += 1

    return steps
