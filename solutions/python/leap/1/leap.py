"""Module for determining a leap year"""
def leap_year(year):
    """Tests if a given year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
