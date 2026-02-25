from random import randint
BugFixMod = False
print('Напишите "камень", "ножницы" или "бумага" так, как написано здесь: без пробелов и с маленькой буквы')
print('Вы можете написать "BugFixMod", чтобы видеть ход бота')
while True:
	bot = randint(1, 3)
	if BugFixMod == True:
		print(bot)
		print("1 - камень, 2 - ножницы, 3 - бумага")	
	player = input("\nВаш выбор: ")
	if player == "BugFixMod":
		if BugFixMod == False:
			BugFixMod = True
			print("BugFixMod on")
		elif BugFixMod == True:
			BugFixMod = False
			print("BugFixMod off")
	if (player == "камень") and (bot == "1"):
		print("Бот выбрал камень и у вас ничья")
	elif (player == "камень") and (bot == "2"):
		print("Бот выбрал ножницы и вы выйграли")
	elif (player == "камень") and (bot == "3"):
		print("Бот выбрал бумага и он выйграл")
	elif (player == "ножницы") and (bot == "1"):
		print("Бот выбрал камень и он выйграл")
	elif (player == "ножницы") and (bot == "2"):
		print("Бот выбрал ножницы и у вам ничья")
	elif (player == "ножницы") and (bot == "3"):
		print("Бот выбрал бумага и вы выйграли")
	elif (player == "бумага") and (bot == "1"):
		print("Бот выбрал камень и вы выйграли")
	elif (player == "бамага") and (bot == "2"):
		print("Бот выбрал ножницы и он выйграл")
	elif (player == "бумага") and (bot == "3"):
		print("Бот выбрал бумага и у вас ничья")
	else:
		print("Вы ввели что-то неверно")