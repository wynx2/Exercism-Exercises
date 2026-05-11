"""Module to translate into Pig Latin"""
def translate(text):
    """Function that receives user input to be translated"""
    phrase_to_translate = text.split(' ')
    translated_phrase = []
    for each_word in phrase_to_translate:
        translated_phrase.append(word_translate(each_word))
    return ' '.join(translated_phrase)
    
def word_translate(text):
    """Function that translates individual words"""
    text_compare = text.upper()
    vowel_list = ('A','E','I','O','U','XR','YT')
    vowel_list2 = ('A','E','I','O','U')
    if text_compare.startswith(vowel_list):
        return f"{text}ay"
    else:
        consonant_list = []
        letter_counter = 0
        q_found = False
        for each_letter in text:
            if each_letter.upper() == 'Q':
                q_found = True
                consonant_list.append(each_letter)
            elif each_letter.upper() == 'U' and q_found:
                q_found = False
                consonant_list.append(each_letter)
                transfer_start = "".join(consonant_list)
                remain_start_list = text.split(transfer_start, 1)
                remain_start = remain_start_list[1]
                return f"{remain_start}{transfer_start}ay"
            elif each_letter.upper() in vowel_list2:
                transfer_start = "".join(consonant_list)
                remain_start_list = text.split(transfer_start, 1)
                remain_start = remain_start_list[1]
                return f"{remain_start}{transfer_start}ay"
            elif each_letter.upper() == 'Y':
                if len(consonant_list) > 0:
                    transfer_start = "".join(consonant_list)
                    remain_start_list = text.split(transfer_start, 1)
                    remain_start = remain_start_list[1]
                    return f"{remain_start}{transfer_start}ay"
                else:
                    consonant_list.append(each_letter)
                    transfer_start = "".join(consonant_list)
                    remain_start_list = text.split(transfer_start, 1)
                    remain_start = remain_start_list[1]
                    return f"{remain_start}{transfer_start}ay"
            else:
                consonant_list.append(each_letter)
            