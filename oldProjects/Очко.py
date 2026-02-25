from random import choice, randint
print('--- Добро пожаловать в \"Очко 21"! ---\nАвтор: Michi The Cat; Специально для: https://t.me/TeaTechnology')
CARDS = [6, 7, 8, 9, 10, 10, 10, 10, 11]*4
Wins, Losses = 0, 0
while True:     # Основной цикл игры
    print(f'\nСтатистика:\nПобед = {Wins}\nПоражений = {Losses}\nВсего игр = {Wins+Losses}')
    while True:
        user = input('\nВыберите действие:\n1. Начать новую игру\n2. Выйти\n> ')
        if user in ['1', '2']: break
        else: print('Такого варианта действий не найдено!')
    if user == '2': break
    elif user == '1':   # Сама игра
        InGameCards = CARDS
        Bot, Player = [InGameCards.pop(randint(0, (len(InGameCards))-1))], []
        while True:
            print(Bot, Player, len(CARDS), len(InGameCards))
            break       # Почему-то обращаясь к InGameCards уменьшается количество CARDS, что странно, ведь к ним не обращаются и они константа... У меня болит голова, займусь кодом позже
input(f'\nСпасибо за игру! За её время вы одержали {Wins} побед и {Losses} поражений... До встречи в следующий раз! ')