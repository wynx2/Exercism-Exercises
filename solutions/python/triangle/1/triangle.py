def equilateral(sides):
    zerp_length = 0
    if zerp_length not in sides:
        if sides[0] == sides[1] and sides[1] == sides[2]:
            return True
    return False


def isosceles(sides):
    sides.sort()
    if sides[0] + sides[1] >= sides[2]:
        if sides[0] == sides[1]:
            return True
        elif sides[0] == sides[2]:
            return True
        elif sides[1] == sides[2]:
            return True
    return False


def scalene(sides):
    if isosceles(sides):
        return False
    else:
        sides.sort()
        if sides[0] + sides[1] < sides[2]:
            return False
    return True
