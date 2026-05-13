"""Check ISBN-10 number"""
def is_valid(isbn):
    """Check ISBN-10 number"""
    valid_digits = ['0','1','2','3','4','5','6','7','8','9','X']
    dcheck = []
    isbn_compressed = isbn.replace('-','')
    for digit in isbn_compressed:
        if digit in valid_digits:
            dcheck.append(digit)
        else:
            return False
    
    dcheck = [10 if digit == 'X' else int(digit) for digit in dcheck]

    if len(dcheck) != 10:
        return False
    if 10 in dcheck and dcheck.index(10) != 9:
        return False
        
        
    result = (dcheck[0] * 10 + dcheck[1] * 9 + dcheck[2] * 8 + dcheck[3] * 7 + dcheck[4] * 6 + dcheck[5]  * 5 + \
            dcheck[6] * 4 + dcheck[7] * 3 + dcheck[8] * 2 + dcheck[9] * 1) % 11

    if result == 0:
        return True
    return False
    
