"""Module to convert base of numbers"""
def rebase(input_base, digits, output_base):
    """Function to convert base of numbers"""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for every_digit in digits:
        if every_digit >= input_base or every_digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")    
    return ten_to_base(base_to_ten(input_base, digits), output_base)

def ten_to_base(number, base_target):
    digit_counter = 0
    digits = list()
    converted_list = list()
    whole_number = int(''.join([str(x) for x in number]))
    while base_target ** digit_counter <= whole_number:
        digits.append(base_target ** digit_counter)
        digit_counter += 1

    number_to_divide = whole_number
    for i in digits[::-1]:
        converted_list.append(number_to_divide // i)
        number_to_divide %= i
    if len(converted_list) == 0:
        converted_list.append(0)
    return(converted_list)

def base_to_ten(input_base, number):
    converted_number_list = number
    converted_number_list.reverse()
    for i in range(len(number)):
        converted_number_list[i] = int(converted_number_list[i]) * (input_base ** i)
    return [int(x) for x in str(sum(converted_number_list))]