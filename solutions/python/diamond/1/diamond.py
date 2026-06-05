"""Module to create a diamond based on a supplied"""
def rows(letter):
    """Function that takes a letter and creates a diamond"""
    letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
            'Q','R','S','T','U','V','W','X','Y','Z']

    scratch_pad = list()
    scratch_pad_2 = list()



    line_size = letter_list.index(letter) * 2 + 1

    for letter_index, letter_value in enumerate(letter_list):
        scratch_pad.append(create_line(letter_index, letter_value, line_size))
        if letter_value == letter:
            break

    for each_line in scratch_pad[-2::-1]:
        scratch_pad.append(each_line)

    return scratch_pad

def create_line(index, passed_letter, size):
    """Function that creates each individual line"""
    new_line = []
    left_point = size // 2 - index
    right_point = size // 2 + index
    for x in range(size):
        if x == left_point or x == right_point:
            new_line.append(passed_letter)
        else:
            new_line.append(' ')
    return ''.join(new_line)


