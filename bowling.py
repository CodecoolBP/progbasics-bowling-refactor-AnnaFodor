def score(game):
    rolls = get_rolls(game)
    result = 0
    roll_id = 0
    for frame in range(0, 10):
        if rolls[roll_id] == 10:
            result += 10 + rolls[roll_id + 1] + rolls[roll_id + 2]
            roll_id += 1
        elif rolls[roll_id] + rolls[roll_id + 1] == 10:
            result += 10 + rolls[roll_id + 2]
            roll_id += 2
        else:
            result += rolls[roll_id] + rolls[roll_id + 1]
            roll_id += 2
    return result


def get_rolls(game):
    rolls = []
    for roll in game.lower():
        if roll == 'x':
            rolls.append(10)
        elif roll == '/':
            rolls.append(10 - rolls[-1])
        elif roll == '-':
            rolls.append(0)
        elif int(roll) > 0 and int(roll) < 10:
            rolls.append(int(roll))
        else:
            raise ValueError()
    return rolls
