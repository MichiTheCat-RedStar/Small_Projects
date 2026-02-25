from random import choice; from time import sleep; money = 100
while True:
	user = input(f'\nУ вас {money}∆\nКакую сумму вы поставите?\n> ')
	try: user = int(user)
	except: print('Введите число!'); continue
	if user > money: print("Недостаточно средстсв!"); continue
	money -= user; print('Крутим...', end='', flush=True); sleep(2.5); x = choice([0.1, 0.5, 0.75, 1, 1.25, 1.50, 2, 3, 5]); money += int(user * x); print('\b'*10, f'Вам выпало: {x}X ({user}∆*{x}->{user*x}∆)\nТеперь ваш счёт: {money}∆')
