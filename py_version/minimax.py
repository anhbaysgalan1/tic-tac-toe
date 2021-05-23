from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
Python хэл дээр MiniMax алгоритмыг ашиглан Tic Tac Toe тоглоомыг бүтээв.
Author: Д.Анхбаясгалан
Year: 2021
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def evaluate(state):
    """
    Төлөв байдлыг эвристик байдлаар үнэлэх.
    :param state: тоглоомын самбарын төлөвийг харуулах
    :return: +1 хэрэв компьютер хожвол; -1 хэрэв тоглогч хожвол; 0 тэнцвэл
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    Энэ функц нь тоглогч хожсон эсэхийг шалгадаг. Боломжууд:
    * Гурван эгнээ    [X X X] or [O O O]
    * Гурван багана    [X X X] or [O O O]
    * Хоёр диагональ [X X X] or [O O O]
    :param state: тоглоомын самбарын төлөвийг харуулах
    :param player: хүн эсвэл компьютер
    :return: Хэрэв тоглогч хожвол True буцаана
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    Энэ функц нь хүн эсвэл компьютер ялсан эсэхийг шалгадаг
    :param state: тоглоомын самбарын төлөвийг харуулах
    :return: Хэрэв тоглогч эсвэл компьютер хожвол True буцаана
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Хоосон нүд бүрийг list-д нэмнэ
    :param state: тоглоомын самбарын төлөвийг харуулах
    :return: хоосон нүднүүдийн жагсаалт
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    Сонгосон нүд хоосон байвал нүүдэл хийх боломжтой болно
    :param x: X координат
    :param y: Y координат
    :return:  хэрэв board[x][y] хоосон бол True буцаана
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Нүүдлийг байршуулна, нүүдлийн координат зөв бол
    :param x: X координат
    :param y: Y координат
    :param player: одоогийн тоглогч
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    хамгийн зөв алхамыг сонгож чадах AI алгоритм
    :param state: тоглоомын самбарын төлөвийг харуулах
    :param depth: tree chart ийн индекс дугаар (0 <= depth <= 9),
    гэхдээ энэ тохиолдолд хэзээ ч ес болохгүй (дараахь функцыг харна уу iaturn())
    :param player: тоглогч эсвэл компьютер
    :return: [хамгийн оновчтой мөр, хамгийн оновчтой багана, хамгийн өндөр оноо]-г агуулсан жягсаалт
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Console ийг цэвэрлэх
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    """
    Console дээр самбарыг хэвлэх
    :param state: тоглоомын самбарын төлөвийг харуулах
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    Хэрэв depth < 9 байвал minimax функцыг дуудна
    бусад тохиолдолд санамсаргүйгээр сонгоно.
    :param c_choice: компьютерийн сонголт X эсвэл O
    :param h_choice: тоглогчийн сонголт X эсвэл O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Компьютерийн нүүдэл [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    """
    Тоглогч боломжит нүүдэл хийсэн эсэх.
    :param c_choice: компьютерийн сонголт X эсвэл O
    :param h_choice: тоглогчийн сонголт X эсвэл O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Тоглогчийн ээлж [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Numpad ашиглана (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Нүүдэл буруу байна')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Баяртай')
            exit()
        except (KeyError, ValueError):
            print('Буруу сонголт байна')


def main():
    """
    Main fункц бүх функцыг ажиллуулна
    """
    clean()
    h_choice = ''  
    c_choice = '' 
    first = ''  

    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('X эсвэл O талын аль нэгийг сонгоно уу\n Таны тал: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Баяртай')
            exit()
        except (KeyError, ValueError):
            print('Буруу нүүдэл')

    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('Тоглоомыг эхлэх үү?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Баяртай')
            exit()
        except (KeyError, ValueError):
            print('Алдаа!')

    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    if wins(board, HUMAN):
        clean()
        print(f'Тоглогчийн ээлж [{h_choice}]')
        render(board, c_choice, h_choice)
        print('ТОГЛОГЧ ХОЖЛОО!')
    elif wins(board, COMP):
        clean()
        print(f'Компьютерийн ээлж [{c_choice}]')
        render(board, c_choice, h_choice)
        print('ТА ХОЖИГДЛОО!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('ТЭНЦЛЭЭ!')

    exit()


if __name__ == '__main__':
    main()