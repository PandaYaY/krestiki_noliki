def analyze(a):

    situation = {
        'horizontal_0': {'O': 0, 'X': 0},
        'horizontal_1': {'O': 0, 'X': 0},
        'horizontal_2': {'O': 0, 'X': 0},
        'vertical_0': {'O': 0, 'X': 0},
        'vertical_1': {'O': 0, 'X': 0},
        'vertical_2': {'O': 0, 'X': 0},
        'diagonal_0': {'O': 0, 'X': 0},
        'diagonal_1': {'O': 0, 'X': 0},
    }

    for string in range(3):  # номера строк
        for column in range(3):  # колонки (элементы строчек)
            if a[string][column] != 0:

                if a[string][column] == 'O':  # заполнение горизонталей
                    situation[f'horizontal_{string}']['O'] += 1
                else:
                    situation[f'horizontal_{string}']['X'] += 1

                if a[string][column] == 'O':  # заполнение вертикалей
                    situation[f'vertical_{column}']['O'] += 1
                else:
                    situation[f'vertical_{column}']['X'] += 1

                if string == column:  # заполнение диагонали
                    if a[string][column] == 'O':
                        situation['diagonal_0']['O'] += 1
                    elif a[string][column] == 'X':
                        situation['diagonal_0']['X'] += 1

                if column + string == 2:  # заполнение второй диагонали
                    if a[string][column] == 'O':
                        situation['diagonal_1']['O'] += 1
                    elif a[string][column] == 'X':
                        situation['diagonal_1']['X'] += 1

    win_line = False
    def_line = False

    for line, item in situation.items():
        if abs(item['X'] - item['O']) == 2:
            if item['X'] == 0:
                win_line = line
                break
            else:
                def_line = line

    if win_line:
        act = two_in_row(a, win_line)
    elif def_line:
        act = two_in_row(a, def_line)
    else:
        act = attack(a)

    return act


def two_in_row(a, line):  # защита
    act = False

    if line == 'horizontal_0':  # по 2 горизонтали
        if a[0][0] == 0:
            act = 11
        elif a[0][1] == 0:
            act = 12
        else:
            act = 13
    if line == 'horizontal_1':  # по 2 горизонтали
        if a[1][0] == 0:
            act = 21
        elif a[1][1] == 0:
            act = 22
        else:
            act = 23
    if line == 'horizontal_2':  # по 3 горизонтали
        if a[2][0] == 0:
            act = 31
        elif a[2][1] == 0:
            act = 32
        else:
            act = 33

    if line == 'vertical_0':  # по 1 вертикали
        if a[0][0] == 0:
            act = 11
        elif a[1][0] == 0:
            act = 21
        else:
            act = 31
    if line == 'vertical_1':  # по 2 вертикали
        if a[0][1] == 0:
            act = 12
        elif a[1][1] == 0:
            act = 22
        else:
            act = 32
    # по 3 вертикали
    if line == 'vertical_2':  # по 3 вертикали
        if a[0][2] == 0:
            act = 13
        elif a[1][2] == 0:
            act = 23
        else:
            act = 33

    if line == 'diagonal_0':  # по 1 диагонали
        if a[0][0] == 0:
            act = 11
        elif a[1][1] == 0:
            act = 22
        else:
            act = 33
    if line == 'diagonal_1':  # по 2 диагонали
        if a[0][2] == 0:
            act = 13
        elif a[1][1] == 0:
            act = 22
        else:
            act = 31

    return act


def first_turn(a):
    if a[1][1] == 'X':  # преимущественно ходит в центр
        act = 11
    else:
        act = 22
    return act


def sub_attack_vertical(a):
    if a[0][1] == 0 and a[2][1] == 0:
        act = 12
    elif a[1][0] == 0 and a[1][2] == 0:
        act = 21
    elif a[1][2] == 0 and a[1][0] == 0:
        act = 23
    elif a[2][1] == 0 and a[0][1] == 0:
        act = 32
    else:
        act = False
    return act


def sub_attack_diagonal(a):
    if a[0][0] == 0 and a[2][2] == 0:
        act = 11
    elif a[0][2] == 0 and a[2][0] == 0:
        act = 13
    elif a[2][0] == 0 and a[0][2] == 0:
        act = 31
    elif a[2][2] == 0 and a[0][0] == 0:
        act = 33
    else:
        act = False
    return act


def attack(a):
    act = False

    if a[0][0] == 0:
        act = 11
    elif a[0][1] == 0:
        act = 12
    elif a[0][2] == 0:
        act = 13
    elif a[1][0] == 0:
        act = 21
    elif a[1][2] == 0:
        act = 23
    elif a[2][0] == 0:
        act = 31
    elif a[2][1] == 0:
        act = 32
    elif a[2][2] == 0:
        act = 33

    if a[1][1] != 'X':
        act = sub_attack_vertical(a) or sub_attack_diagonal(a) or act
    else:
        act = sub_attack_diagonal(a) or sub_attack_vertical(a) or act

    return act


def bot(place, turn):
    act = 0
    if turn == 2:  # первый ход бота
        act = first_turn(place)
    if turn > 3:
        act = analyze(place)
    string = act // 10 - 1
    column = act % 10 - 1
    return string, column
