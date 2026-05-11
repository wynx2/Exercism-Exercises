def is_armstrong_number(number):
    """This is a function that tests if a number is an Armstrong number"""
    result = 0
    list_of_numbers = [int(numeral) for numeral in (str(abs(number)))]
    for digit in list_of_numbers:
        result += digit ** len(list_of_numbers)
    if result == number:
        return True
    return False
    
