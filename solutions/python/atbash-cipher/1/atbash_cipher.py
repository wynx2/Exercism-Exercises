"""Module that applies Atbash Cipher"""
def encode(plain_text):
    """Function to encode Atbash Cipher"""
    plain = ['a','b','c','d','e','f','g','h','i','j','k',
             'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipher = plain[::-1]
    cipher_holding = []
    encode_counter = 0

    for each_letter_position in range(len(plain_text)):
        if plain_text[each_letter_position] == ' ':
            continue
        if encode_counter == 5:
            cipher_holding.append(' ')
            encode_counter = 0
        try:
            cipher_holding.append(cipher[plain.index(plain_text[each_letter_position].lower())])
            encode_counter += 1
        except:
            if plain_text[each_letter_position].isnumeric():
                cipher_holding.append(plain_text[each_letter_position])
                encode_counter += 1
    if cipher_holding[-1] == ' ':
        cipher_holding.pop()
    return ''.join(cipher_holding)


def decode(ciphered_text):
    """Function that decodes Atbash Cipher"""
    plain = ['a','b','c','d','e','f','g','h','i','j','k',
             'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipher = plain[::-1]

    plain_holding = []
    pre_decipher = ciphered_text.replace(' ','')

    for each_letter_position in range(len(pre_decipher)):
        try:
            plain_holding.append(plain[cipher.index(pre_decipher[each_letter_position].lower())])
        except:
            plain_holding.append(pre_decipher[each_letter_position])
    return ''.join(plain_holding)
