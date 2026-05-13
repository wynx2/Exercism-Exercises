"""Checks if a sentence is a pangram"""
def is_pangram(sentence):
    """This function checks if a sentence is a pangram"""
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_counter = 0
    for each_letter in alphabet:
        if each_letter in sentence.lower():
            continue
        else:
            letter_counter+=1
    if letter_counter > 0:
        return False
    return True
