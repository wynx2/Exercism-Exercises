def is_paired(input_string):
    bracket_count = 0
    brace_count = 0
    parentheses_count = 0

    close_sequence = list()

    string_queue = list(input_string)

    for each_character in string_queue:
        if each_character == '{':
            brace_count += 1
            close_sequence.append(set_close(each_character))
        if each_character == '(':
            parentheses_count += 1
            close_sequence.append(set_close(each_character))
        if each_character == '[':
            bracket_count += 1
            close_sequence.append(set_close(each_character))
        if each_character == '}':
            try:
                if close_sequence.pop() == each_character:
                    brace_count -= 1
            except:
                return False
        if each_character == ')':
            try:
                if close_sequence.pop() == each_character:
                    parentheses_count -= 1
            except:
                return False
        if each_character == ']':
            try:
                if close_sequence.pop() == each_character:
                    bracket_count -= 1
            except:
                return False
        if close_no_open(brace_count, bracket_count, parentheses_count):
            return False
        

    if brace_count + bracket_count + parentheses_count == 0:
        return True

    return False
    
def close_no_open(counter_1, counter_2, counter_3):
    if counter_1 < 0:
        return True
    if counter_2 < 0:
        return True
    if counter_3 < 0:
        return True
    
    return False

def set_close(symbol):
    symbol_dict = {'(':')',
                   '{':'}',
                   '[':']',}

    return symbol_dict[symbol]

