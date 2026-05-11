def square(number):
    """Compute grains on square"""
    square_number = []
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    for i in range(number):
        if i == 0:
            square_number.append(1)
        else:
            square_number.append(square_number[-1]*2)

    return square_number[-1]


def total():
    total_number = 0
    for i in range(1,65):
        total_number += square(i)
    return total_number
    
    
