"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    orig_order = list()
    if len(list_one) == 0 and len(list_two) > 0:
        return SUBLIST
    if len(list_two) == 0 and len(list_one) > 0:
        return SUPERLIST
    if list_one == list_two:
        return EQUAL
    if len(list_one) < len(list_two):
        for each_number in range(len(list_two)-len(list_one)+1):
            for each_number_compare in range(len(list_one)):
                if list_two[each_number+each_number_compare] != list_one[each_number_compare]:
                    break
            else:
                return SUBLIST
    if len(list_two) < len(list_one):
        for each_number in range(len(list_one)-len(list_two)+1):
            for each_number_compare in range(len(list_two)):
                if list_one[each_number+each_number_compare] != list_two[each_number_compare]:
                    break
            else:
                return SUPERLIST
    return UNEQUAL
    
    
