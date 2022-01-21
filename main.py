import os
from bot import bot


def win(a):
    if (
            (a[0][0] == a[0][1] == a[0][2] != 0) or
            (a[1][0] == a[1][1] == a[1][2] != 0) or
            (a[2][0] == a[2][1] == a[2][2] != 0) or

            (a[0][0] == a[1][0] == a[2][0] != 0) or
            (a[0][1] == a[1][1] == a[2][1] != 0) or
            (a[0][2] == a[1][2] == a[2][2] != 0) or

            (a[0][0] == a[1][1] == a[2][2] != 0) or
            (a[0][2] == a[1][1] == a[2][0] != 0)
    ):
        return True
    else:
        return False


def try_input(a):
    mistake = False
    while True:
        print_place(a)
        if mistake:
            print(mistake)

        try:  # защита от текста
            act = int(input('Ваш ход(11, 13...(строка, столбец): '))
        except ValueError:
            mistake = 'Это не цифры!!!'
            continue

        string = act // 10 - 1
        column = act % 10 - 1

        if not(act in [11, 12, 13, 21, 22, 23, 31, 32, 33]):  # если написал не ячейку
            mistake = 'Таких ячеек нет на поле!!!'
            continue
        elif a[string][column] != 0:
            mistake = 'Эта ячейка занята!!!'
            continue
        else:
            return string, column


def one_player_step(a, player):  # для игры с ботом
    if player % 2 == 1:
        string, column = try_input(a)
        a[string][column] = 'X'
    else:
        string, column = bot(a, player)
        a[string][column] = 'O'


def two_player_step(a, player):  # для 2-х игроков
    string, column = try_input(a)
    if player % 2 == 1:
        a[string][column] = 'X'
    else:
        a[string][column] = 'O'


def print_place(a):
    os.system('cls')  # очистка экрана
    for string in a:
        print('-' * 13 + '\n|', end='')
        for i in string:
            if i == 0:
                i = '-'
            print(f' {i} |', end='')
        print()
    print('-' * 13)


def game(mode):
    place = [[0 for _ in range(3)] for _ in range(3)]
    turn = 0
    while True:
        turn += 1
        if mode == 1:
            one_player_step(place, turn)
        else:
            two_player_step(place, turn)

        if turn > 4 and win(place):
            print_place(place)
            winner = turn % 2
            if winner == 1:
                print(f'Победили крестики')
            else:
                print(f'Победили нолики')
            break

        elif turn == 9:
            print_place(place)
            print('Победила ничья.')
            break


cmd = 'mode 40, 10'
os.system(cmd)

while True:
    print('Игра "Крестики нолики"\n'
          'Выберите режим игры:\n'
          '1. На одного игрока(против компьютера)\n'
          '2. На двух игроков\n'
          '3. Выход')

    try:  # проверка на ошибки
        game_mode = int(input('Ввод: '))
    except ValueError:
        os.system('cls')
        print('Это не цифры!!!')
        continue
    if game_mode not in [1, 2, 3]:
        os.system('cls')
        print('Не те цифры...')
        continue

    if game_mode == 3:
        break

    while True:
        game(game_mode)
        repeat = input('Желаете повторить партию?(y/n): ').lower()
        if repeat == 'y':
            continue
        else:
            os.system('cls')
            break
