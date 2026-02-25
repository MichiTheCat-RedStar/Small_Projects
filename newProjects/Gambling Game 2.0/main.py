from random import choice; from time import sleep
money, debt = 100, 0
try:
	with open('save', 'r', encoding='UTF-8') as f: f = f.read(); f = f.split('\n'); money = int(f[0]); debt = int(f[1])
except: print('Сохранение не найдено\nНапишите "Сохранить" для сохранения')
else: print('Сохранение загружено\nНапишите "Сохранить" для сохранения')

while True:
	user = (input(f'\nУ вас {money}∆ и долг {debt}∆\nКакую сумму вы поставите?\n> ') if debt else input(f'\nУ вас {money}∆\nКакую сумму вы поставите?\n> '))
	if user.lower() in ['сохранить', 'save', 's', 'с']:
		with open('save', 'w', encoding='UTF-8') as f: f.write(f'{money}\n{debt}'); print('Сохранено!'); continue
	try: user = int(user)
	except: print('Введите число!'); continue
	if user > money: print("Недостаточно средств!"); continue
	if user < 0: debt += user*-1; money += user*-1; print(f'Вы взяли в долг {user*-1}∆'); continue

	money -= user; print('Крутим...', end='', flush=True); sleep(2.5)
	x = choice([0.1, 0.5, 0.75, 1, 1.25, 1.50, 2, 3, 5]); money += int(user * x)
	print('\r', f'Вам выпало: {x}X ({user}∆*{x}->{user*x}∆)\nТеперь ваш счёт: {money}∆')
	if debt and money > debt: money -= debt; debt = 0; print('Ваш долг насильно погашен!')