#		dialog_text // ☭
# MichiTheCat-RedStar (c) 2026

from time import sleep


# show
def show(*text:str, delay=0.1, end='\n') -> None:
	'''Вывод текста красиво, постепенно'''
	text = ' '.join(text)
	text = list(text)
	for c in text:
		print(c, end='', flush=True)
		sleep(delay)
	print(end=end)

# question
def question(question_text:str, options:list, cursor='> ', wrong_message='Такого варианта нет в списке! Выберите вариант из списка!', end='\n') -> str:
	'''Вопрос пользователю с вариантами ответа'''
	while True:
		print(question_text)
		for option_index in range(len(options)):
			print(f'{option_index+1}. {options[option_index]}')
		User = input(cursor)
		try:
			User = int(User)-1
			if User < 0:
				print(wrong_message)
				print(end=end)
				continue
			User = options[User]
		except ValueError:
			print(wrong_message)
		except IndexError:
			print(wrong_message)
		else:
			return str(User)
		print(end=end)


# Test
if __name__ == '__main__':
	show('Привет', 'Мир!', end='')
	show(str(123))
	show('А сейчас будет интересный вопрос для вас...')
	show('\nГотовы???\n', delay=0.5)
	print('\nВыбрали:', question('Любишь этот код?', ['Да', 'Не знаю', 'Нет']), '\n')
	
	print('\nУдачи!' if question('Уходите?', ['Да', 'Нет']) == 'Да' else '\nНет, вы уходите!')
