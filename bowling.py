def score(game):
    result = 0
    frame = 1
    in_first_half = True
    last = 0
    for roll in range(len(game)):
        result += roll_score(game[roll], get_value(game[roll]), last)
        if frame < 10 and get_value(game[roll]) == 10:
            result += get_value(game[roll+1])
            if game[roll].lower() == 'x':
                result += roll_score(game[roll+2], get_value(game[roll+2]), get_value(game[roll+1]))
        last = get_value(game[roll])
        if in_first_half:
            in_first_half = not in_first_half
        else:
            in_first_half = True
            frame += 1
        if game[roll].lower() == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char in "123456789":
        return int(char)
    elif char.lower() in "x/":
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def roll_score(try_to_check, actual_try_points, last_try_points):
    if try_to_check == '/':
        return 10 - last_try_points
    else:
        return actual_try_points
