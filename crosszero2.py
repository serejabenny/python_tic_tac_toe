# 1. Создаем поле игры ( field )
# 2. Указываем победные комбинации ( win_combinations )
# 3. Функции : 1) Вывод поля 2) Ход 3) Победные комбинации
# 4. Код игры

print("Игра Крестики-Нолики")
field = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

win_combinations = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8],
                    [2, 4, 6]]

def print_field():
    print(field[0], end = " ")
    print(field[1], end = " ")
    print(field[2])

    print(field[3], end = " ")
    print(field[4], end = " ")
    print(field[5])

    print(field[6], end = " ")
    print(field[7], end = " ")
    print(field[8])

def step_field(step,symbol):
    ind = field.index(step)
    field[ind] = symbol

def result_combinations():
    win = ""

    for i in win_combinations:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]]  == "X" :
            win = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O" :
            win = "O"
    return win


game = False
player1 = True
counter = 0
while game == False:

    print_field()

    if counter % 2 ==0:
        symbol = "X"
        step = int(input("Первый Игрок ваш ход :" ))
    else:
        symbol="O"
        step = int(input("Второй Игрок ваш ход :"))

    counter += 1

    if counter == 9:
        print(" Ничья! ")
        break


    step_field(step, symbol)
    win = result_combinations()

    if win != "":
        game = True
    else:
        game = False

    player1 = not(player1)

print_field()
print("Победил ", win)












