"""Module for Bob's response"""
def response(hey_bob):
    """Function that returns Bob's response"""
    test_string = hey_bob.strip()
    if test_string.isspace() or test_string == "":
        return 'Fine. Be that way!'
    if test_string.endswith('?'):
        if test_string.isupper():
            return 'Calm down, I know what I\'m doing!'
        return 'Sure.'
    if test_string.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'
