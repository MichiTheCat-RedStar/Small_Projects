START_COMMAND = 'RUN'					# Старт слово					<- Запускает выполнение кода
START_WITH_SAVE_COMMAND = 'RUN SAVE'	# Старт слово с сохранением		<- Запускает выполнение кода и перед этим сохраняет в файл
LOAD_COMMAND = 'RUN LOAD'				# Старт слово с загрузкой		<- Запускает выполнение кода и перед этим загружает из файла
words = [
	('вывести', 'print'),
	('если', 'if'), ('иначе', 'else'), ('иначе если', 'elif'),
	('постоянно', 'while'),
	('Верно', 'True'), ('Ложно', 'False'),
	('строка', 'str'), ('число', 'int'), ('список', 'list'), ('словарь', 'dict'), ('булево', 'bool'), ('плавающее', 'float'), ('количество', 'len'),
	('в', 'in'), ('для', 'for'), ('диапазон', 'range'),
	('ввод', 'input'), ('лямбда', 'lambda'),
	('импорт', 'import'),
	('прервать', 'break'), ('вернуть', 'return'), ('пропустить', 'pass'), ('продолжить', 'continue'), ('остановить', 'quit'),
	('и', 'and'), ('или', 'or'), ('не', 'not'),
	('функиця', 'def'), ('класс', 'class'), ('локально', 'locals'), ('глобально', 'globals'),
	('разделить', 'split'), ('меньше', 'lower'), ('больше', 'upper'), ('присоеднить', 'join'), ('заменить', 'replace')
]

# Код полностью создан MichiTheCat для https://t.me/TeaTechnology // Версия 1.3 [Пометка для себя: продолжай дальше обновлять в 1.3, я ещё его не выпустил]

words = (sorted(words, key=lambda size: len(size[0])))[::-1]
print(f'Напишите "{START_COMMAND}" для запуска кода, "{START_WITH_SAVE_COMMAND}" для его сохранения и запуска или "{LOAD_COMMAND}" для загрузки (или "help" для помощи) (на данный момент здесь {len(words)} слов):')
line, full_code, code = 1, '', ''

# Пометка для 1.3 (Пс, Michi из будущего, замени это на что-то нормальное) // 19.10.25 - услышал тебя прошлый я, ща
while (code != START_COMMAND) and (code != START_WITH_SAVE_COMMAND) and (code != LOAD_COMMAND): # Основной цикл, где пользователь вводит код и запускает
	code = input(f'{line}> ')
	full_code += f'\n{code}'
	line += 1
	if code == START_COMMAND:
		full_code = full_code[:-(len(START_COMMAND))]
	elif code == START_WITH_SAVE_COMMAND:
		full_code = full_code[:-(len(START_WITH_SAVE_COMMAND))]
		with open(f'{input('Дайте имя файлу> ')}.rupy', 'w', encoding='UTF-8') as file:
			file.write(full_code[1:-1])
	elif code == LOAD_COMMAND:
		with open(f'{input('Название файла> ')}.rupy', 'r', encoding='UTF-8') as file:
			full_code = file.read()
	if (code == 'help') or (code == 'h') or (code == 'помогите') or (code == 'помощь'):
		for translate in words: print(f'{translate[0]} \t-> \t{translate[1]}')

'''for translate in words: full_code = full_code.replace(translate[0], translate[1]) # Заменяет слова на понятные питону''' # Заменить на нормальное конвертирование
for char in full_code:
	print(char) # тут в 1.3 допиши короче

print('Запуск...') # Запускает код как питоновский
try: exec(full_code, {}, {})
except Exception as error: input(f'{error} ')
else: input('[Код завершил работу] ')