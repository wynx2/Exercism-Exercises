"""Module to test if a word or phrase is an isogram"""
def is_isogram(string):
    """Function to test if a word or phrase is an isogram"""
    new_string = string.replace('-','')
    new_string2 = new_string.replace(' ', '')

    characters_used = []

    for each_character in new_string2:
        if each_character.lower() in characters_used:
            return False
        characters_used.append(each_character.lower())
    return True

       
