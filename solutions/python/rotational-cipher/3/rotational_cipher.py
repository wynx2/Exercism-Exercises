"""Module that implements a rotational cipher"""
def rotate(text, key):
    """Function that implements a rotational cipher"""
    plain_cipher_string = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    plain_cipher = list(plain_cipher_string)

    cipher_dict = {}

    for each_character in range(26):

        cipher_dict[plain_cipher[each_character]] = plain_cipher[each_character + key]

    cipher_text = []
    for old_letter in text:
        if old_letter.lower() in cipher_dict:
            if old_letter.isupper():
                cipher_text.append(cipher_dict[old_letter.lower()].upper())
            else:
                cipher_text.append(cipher_dict[old_letter])
        else:
            cipher_text.append(old_letter)

    return ''.join(cipher_text)