def is_armstrong_number(number):
    result = 0
    list_of_numbers = [int(x) for x in (str(abs(number)))]
    for digit in list_of_numbers:
        result += digit ** len(list_of_numbers)
    if result == number:
        return True
    else:
        return False
    
