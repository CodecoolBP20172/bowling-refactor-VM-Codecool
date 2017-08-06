def score(game):
    result = 0
    frame = 1
    game_is_on = True
    for roll in range(len(game)):
        if game[roll] == '/':
            result += 10 - get_value(game[roll-1])
        else:
            result += get_value(game[roll])
        if frame < 10 and get_value(game[roll]) == 10:
            if game[roll] == '/':
                result += get_value(game[roll+1])
            elif game[roll] == 'X' or game[roll] == 'x':
                result += get_value(game[roll+1])
                if game[roll+2] == '/':
                    result += 10 - get_value(game[roll+1])
                else:
                    result += get_value(game[roll+2])
        if game[roll] == 'X' or game[roll] == 'x' or not game_is_on:
            frame += 1
            game_is_on = True
        else:
            game_is_on = False
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

score("XXXXXXXXXXXX")
