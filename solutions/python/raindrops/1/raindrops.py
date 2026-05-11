def convert(number):
    myseparator = ''
    string_container = []
    divisible_flag = False
    if number % 3 == 0:
        string_container.append('Pling')
        divisible_flag = True
    if number % 5 == 0:
        string_container.append('Plang')
        divisible_flag = True
    if number % 7 == 0:
        string_container.append('Plong')
        divisible_flag = True
    if divisible_flag:
        return myseparator.join(string_container)
    return str(number)
        
    
