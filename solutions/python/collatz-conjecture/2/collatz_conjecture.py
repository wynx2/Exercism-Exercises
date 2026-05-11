def steps(number):
    """ this returns the number of steps for the Collatz Conjecture exercise."""
    number_of_steps = 0
    operation_result = number
    if operation_result <= 0:
        raise ValueError("Only positive integers are allowed")
    while operation_result != 1:
        if operation_result % 2 == 0:
            operation_result/= 2
        else:
            operation_result = (operation_result * 3) + 1

        number_of_steps += 1

    return number_of_steps
