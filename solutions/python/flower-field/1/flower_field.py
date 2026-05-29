"""Module that implements Flower Field"""
def annotate(garden):
    """Function that annotates garden field"""
    f_field = list()
    check_malformed(garden)
    for garden_element in garden:

        f_field.append(list(garden_element))

    for yLane in range(len(f_field)):
        for xLane in range(len(f_field[yLane])):
            if f_field[yLane][xLane] == '*':
                for ySweeper in range(yLane - 1, yLane + 2):
                    if ySweeper < 0 or ySweeper == len(f_field):
                        continue
                    for xSweeper in range(xLane - 1, xLane + 2):
                        if xSweeper < 0 or xSweeper == len(f_field[yLane]):
                            continue
                        if isinstance(f_field[ySweeper][xSweeper],int):
                            f_field[ySweeper][xSweeper] += 1
                        if f_field[ySweeper][xSweeper] == ' ':
                            f_field[ySweeper][xSweeper] = 1
            elif isinstance(f_field[yLane][xLane], int) or f_field[yLane][xLane] == ' ':
                continue
            else:
                raise ValueError("The board is invalid with current input.")


    annotated_field = list()

    for each_lane in f_field:
        for each_item in range(len(each_lane)):
            if isinstance(each_lane[each_item], int):
                each_lane[each_item] = str(each_lane[each_item])
        annotated_field.append(''.join(each_lane))

    return annotated_field

def check_malformed(garden):
    for element in range(len(garden)):
        if len(garden[0]) != len(garden[element]):
            raise ValueError("The board is invalid with current input.")
